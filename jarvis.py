
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# can also print other voice - (voices[1].id)                 
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
  
  hour = int(datetime.datetime.now().hour)

  if hour>=0 and hour<12:
   speak("Good Morning!")

  elif hour>=12 and hour<19:
   speak("good afternoon!")

  else:
   speak("Good Evening!")

  speak("I am Jarvis Mam. Please tell me how may I help you ")

def takeCommand(): 
  # it takes microphone input from the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
     print("Listening.....")
     r.pause_threshold = 1
     audio = r.listen(source)
   #   query = r.recognize_google(audio, Language = 'en-in')
   #   print(f"User said: {query}") 
   #   query = r.recognize_google_cloud(audio, language="en-in")


  try:
      print("Recognizing...")
      query = r.recognize_google(audio, language = 'en-in')
      print(f"User said: {query} ")  

  except Exception as e:
      
      print("Say that again please...")
      return "None"
  return query


if __name__=="__main__":
      wishMe()
      while True:
         query = takeCommand().lower()
   
        #logic for executing tasks based on query
         if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
 
         elif  'open youtube' in query:
            webbrowser.open("youtube.com")

         elif  'open google' in query:
            webbrowser.open("google.com")

         elif 'open stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")

         elif 'play music' in query:
            music_dir = 'C:\\Users\\RITESH MOHITE\\OneDrive\\Desktop\\Jarvis Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

              

        