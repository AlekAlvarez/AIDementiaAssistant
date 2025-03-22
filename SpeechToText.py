import speech_recognition as sr
recognizer = sr.Recognizer()

#audio_file = sr.AudioFile('path_to_your_audio_file.wav')

import speech_recognition as sr

# Create recognizer instance
r = sr.Recognizer()

# Start listening to the microphone
def listen():
        with sr.Microphone() as source:
            print("Say 'stop' to end recording.")
            
            # Adjust for ambient noise (optional, can improve recording quality)
            r.adjust_for_ambient_noise(source)

            while True:
                audio = r.listen(source)
                
                # Recognize speech using Google Speech Recognition
                text = r.recognize_google(audio)
                print("Transcription: " + text)

                # Save the transcribed text into a .txt file (append mode to avoid overwriting)
                with open("transcribed_text.txt", "a") as text_file:
                    text_file.write(text + "\n")  # Write the text into the file with a newline, this text file 
                                                # will be passed into Gemini

                # Check if 'stop' is in the transcribed text to stop recording
                if "goodbye" in text.lower():
                    print("Stopping recording...")
                    break