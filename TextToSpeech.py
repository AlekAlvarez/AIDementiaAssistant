#depends on gTTS package
from gtts import gTTS
#depends on vlc and you must have vlc installed
import vlc
import time
from mutagen.mp3 import MP3
def get_mp3_duration(file_path):
    audio = MP3(file_path)
    return audio.info.length
def playText(textToConvert,language='en'):
    converter=gTTS(text=textToConvert,lang=language,slow=False)
    converter.save("ThrowAway.mp3")
    duration=get_mp3_duration("ThrowAway.mp3")
    p = vlc.MediaPlayer("ThrowAway.mp3")
    p.play()
    while p.is_playing():
        time.sleep(0.1)