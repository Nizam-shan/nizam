import pyttsx3
#engine = pyttsx3.init()
#engine.say("hi how are you")
#engine.runAndWait()

n = input("enter the number")
dict = { 
    "1" : "ones",
    "2" : "twos",
    "3" : "threes",
    "4" : "fours",
    "5" : "fives",
    "6" : "sixs",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10" : "tens"
}
text=""
for i in range(1,11):
    mul=i*int(n)
    text+= str(i)+" " +dict[n]+" are " +str(mul) +"\n"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
