from flask import Flask, render_template, json, request, jsonify, redirect, url_for
from flask_cors import CORS
from google import genai
import os
from TextToSpeech import playText
from SpeechToText import listen
from mood_analysis import analyze_sentiment
from google.genai import types
import threading
import time
gConv=""
login=False
file=open("flaskData.json")
gD=json.load(file)
file.close()
talking=False
gConv="Doctors Notes: Family Member INFO: "+gD["familyMembers"]+"Patient Hobbies: "+gD["hobbies"]
gConv+="Medications: "+gD["medications"]
gPatient=gD['patientName']
my_api_key = os.getenv('GEN_AI_API_KEY')
client = genai.Client(api_key=my_api_key)
chat = client.chats.create(model="gemini-2.0-flash")
def nlp():
    time.sleep(5)
    while 1==1:
        conv_history=gConv
        patientName=gPatient
        listen()
        req=""
        with open("transcribed_text.txt") as file:
            req=file.read()
        open("transcribed_text.txt", 'w').close()
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Doctors info follows: ",conv_history,"what follows is a patient question", req],
        config=types.GenerateContentConfig(
            system_instruction="You are the care companion of a dementia patient. Please respond by answering from the previolsy provided chat history. Please address the patient by their name which is "+patientName
            ,max_output_tokens=100,
            temperature=0.5)
        )
        talking=True
        playText(response.text) 
        talking=False
        tup=analyze_sentiment(req)
        sentiment_category=tup[1]
        newInfo=client.models.generate_content(
            model="gemini-2.0-flash",
            contents=["Previous History follows:",conv_history,"Does the next string have any information about the patient not in the previous string respond with None if there is no new info or with a summary of the new info",req]
            ,config=types.GenerateContentConfig(system_instruction="If there is no new info only respond with None one word do not exced one word unless there is new info")
        )
        newData=""
        if newInfo.text[0]!='N':
            conv_history+=newInfo.text
            newData=newInfo.text
        with open("patientInterfaceData.json",'w') as f:
            d={ "modificationRequest": newData, "mood": sentiment_category}
            json.dump(d,f)
        print(sentiment_category)
        print(response.text)
app = Flask(__name__,template_folder="./templates")
CORS(app)
@app.route('/')
def index():
    #Flask load example
    return render_template('./portal.html')
@app.route("/loadData")
def load_data():
    print("HI")
    file=open("flaskData.json")
    result=json.load(file)
    file.close()
    print("c")
    
    return result
@app.route('/DataToServer', methods=['POST'])
def api_data():
    # Access data sent as JSON in the body of the request
    data = request.get_json()  # Parse the incoming JSON data
    while(talking):
        time.sleep(5)
    with open('flaskData.json', 'w') as f:
        json.dump(data, f)
    result={"transmitted":True}
    return jsonify(result)
@app.route("/login", methods=['POST'])
def login():
    data=request.get_json()
    print(data)
    login=True
    print("what is wrong")
    return render_template("portal.html")
@app.route("/DataToPortal")
def get_data():
    while(talking):
        time.sleep(5)
    file=open("patientInterfaceData.json")
    result=json.load(file)
    file.close()
    with open("patientInterfaceData.json",'w') as f:
        d={ "modificationRequest": "", "mood": ""}
        json.dump(d,f)
    return result
if __name__ == '__main__':
    thread = threading.Thread(target=nlp,daemon=True)
    thread.start()
    app.run(host='0.0.0.0', debug=True)