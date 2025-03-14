import speech_recognition as sr

r = sr.Recognizer()

while True: 
  try: 
      with sr.Microphones() as source: 
    print("ask something")
    audio = r.Listen(source)
    text = r.recognize_google(audio)
    text = text.lower()

    print(f"Recognized text : {text}")

except: 
  print("Your were trying to be funny")
  r = sr.Recognizer()
  continue
