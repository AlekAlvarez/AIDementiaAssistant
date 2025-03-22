from google import genai
import os
from TextToSpeech import playText
from SpeechToText import listen
my_api_key = os.getenv('GEN_AI_API_KEY')
client = genai.Client(api_key=my_api_key)
chat = client.chats.create(model="gemini-2.0-flash")
conv_history=["The patient's brother is away for the day"]
while 1==1:
    listen()
    req=""
    with open("transcribed_text.txt") as file:
        req=file.read()
    open("transcribed_text.txt", 'w').close()
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[req],
    history=conv_history,
    config=types.GenerateContentConfig(
        system_instruction="You are the care companion of a dementia patient. Please respond by answering from the previolsy provided chat history. Have the first line of you response be either Yes or No followed by a new line Yes if the information was in the provided history No if it was not"
        ,max_output_tokens=100,
        temperature=0.1)
    )
    lines=response.split("\n")
    if lines[0][0]=="N":
        history.append(request)
    playTex(response)