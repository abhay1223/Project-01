import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()

def SpeakText(command):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)

  engine.say(command)
  engine.runAndWait()

while(1):    
     
    
    try:
         
     
        with sr.Microphone() as source2:
             
          
            r.adjust_for_ambient_noise(source2, duration=0.2)
          
            audio2 = r.listen(source2)
             
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print(MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")