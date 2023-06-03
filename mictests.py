import speech_recognition as sr

#instantiate recognizer and mic objects
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

#instantiate interpretation log file
sttlog = open("speechtotextlogwhisper.txt","w")

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
            #trying a number of different stt models... Trying to find best for purpose.
            #defectbroadcast = r.recognize_vosk(audio)
            #defectbroadcast = r.recognize_google(audio)
            defectbroadcast = r.recognize_whisper(audio, model = "small") #model attribute is whichever is preferred in the OpenAI Whisper docs. Default is base for SpeechRecognition library.
            sttlog.write(defectbroadcast + "\n")
            print("interpreted as " + defectbroadcast)
        except:
            print("there was an error interpreting the speech. Please try again.")
except KeyboardInterrupt:
    print("Program exited successfully")
    sttlog.close()
    


