import speech_recognition as sr

#instantiate recognizer and mic objects
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

#instantiate interpretation log file
sttlog = open("speechtotextlog","w")

#configure the recognizer instance
#make the pause threshold longer because the default cuts off at "no defects"
r.pause_threshold = 3

try:
    while(True):
        #listen for word
        with mic as source:
            print("listening...")
            audio = r.listen(source,timeout = None)
        print("heard, processing...")
        #interpret the audio, using a try to handle case where STT fails
        try:
            # TODO swap speech recognition to Vosk
            defectbroadcast = r.recognize_google(audio)
            sttlog.write(sttlog + "\n")
            print("interpreted as " + defectbroadcast)
        except:
            print("there was an error interpreting the speech. Please try again.")
except KeyboardInterrupt:
    print("Program exited successfully")
    sttlog.close()
    


