import speech_recognition as sr

#instantiate recognizer and mic objects
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

#configure the recognizer instance
#make the pause threshold longer because the default cuts off at "no defects"
r.pause_threshold = 3

while(True):
    #listen for word
    with mic as source:
        print("listening...")
        audio = r.listen(source,timeout = None)
    print("heard, processing...")
    #interpret the audio, using a try to handle case where STT fails
    try:
        defectbroadcast = r.recognize_google(audio)
        print("interpreted as " + defectbroadcast)
    except:
        print("there was an error interpreting the speech. Please try again.")


