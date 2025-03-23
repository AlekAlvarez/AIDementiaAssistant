from google import genai
import os
from TextToSpeech import playText
from SpeechToText import listen
from mood_analysis import analyze_sentiment
from google.genai import types
my_api_key = os.getenv('GEN_AI_API_KEY')
client = genai.Client(api_key=my_api_key)
chat = client.chats.create(model="gemini-2.0-flash")
conv_history="In his anger he pushed Padme his wife away"
patientName="Anakin"
while 1==1:
    #listen() TODO
    req=""
    with open("transcribed_text.txt") as file:
        req=file.read()
    open("transcribed_text.txt", 'w').close()
    req=input()
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Doctors info follows: ",conv_history,"what follows is a patient question", req],
    config=types.GenerateContentConfig(
        system_instruction="You are the care companion of a dementia patient. Please respond by answering from the previolsy provided chat history. Please address the patient by their name which is "+patientName
        ,max_output_tokens=100,
        temperature=0.5)
    )
    #playTex(response) TODO
    tup=analyze_sentiment(req)
    sentiment_category=tup[1]
    newInfo=client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Previous History follows:",conv_history,"Does the next string have any information about the patient not in the previous string respond with None if there is no new info or with a summary of the new info",req]
        ,config=types.GenerateContentConfig(system_instruction="If there is no new info only respond with None one word do not exced one word unless there is new info")
    )
    print(newInfo.text)
    print(sentiment_category)
    print(response.text)