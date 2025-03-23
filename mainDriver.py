from flask import Flask, render_template, json, request, jsonify
from flask_cors import CORS
from google import genai
import os
from TextToSpeech import playText
from SpeechToText import listen
from mood_analysis import analyze_sentiment
from google.genai import types
import threading
import queue
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
    with open('flaskData.json', 'w') as f:
        json.dump(data, f)
    result={"transmitted":True}
    return jsonify(result)
@app.route("/DataToPortal")
def get_data():
    file=open("patientInterfaceData.json")
    result=json.load(file)
    file.close()
    with open("patientInterfaceData.json",'w') as f:
        d={ "modificationRequest": "", "mood": ""}
        json.dump(d,f)
    return result
if __name__ == '__main__':
    thread = threading.Thread(target=background_task,daemon=True)
    thread.start()
    app.run(host='0.0.0.0', debug=True)