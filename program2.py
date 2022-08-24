
from gtts import gTTS
from playsound import playsound
import io

#token = input("enter the token")
#txt="ടോക്കൺ നമ്പർ" + token
#ob=gTTS(txt,lang = 'ml')
#ob.save("token.mp3")
#playsound("token.mp3")
fp = io.open("book.text",mode='r',encoding="utf-8")
book_content=fp.read()
ob=gTTS(book_content,lang = 'ml')
ob.save("book.mp3")
playsound("book.mp3")
