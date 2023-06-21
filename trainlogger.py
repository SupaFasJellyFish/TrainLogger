import speech_recognition as sr
import sqlite3
from datetime import datetime

#dict for common number misinterpretations by Whisper STT.
worddigit = {"zero":"0","one":"1","two":"2","to":"2","too":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","niner":"9","9R":"9"}

#Table for letter and punctuation removal operations
filtertable = str.maketrans("","","abcdefghijklmnopqrstuvwxyz.,? !-_|/")

#Class to store data about a train
class train:
    def __init__(self, length, track, defect):
        self.length = length
        self.track = track
        self.defect = defect

#SQL table schema (for reference):CREATE TABLE trains( timestamp DATETIME, axles INTEGER, defect TEXT NOT NULL, broadcast TEXT NOT NULL, track TEXT_NOT_NULL); 

#Prep sql database for I/O
dbconnection = sqlite3.connect("TrainLogger/trains.db")
dbcursor = dbconnection.cursor()

#set up text log for diagnostics in case interpretation fails. 
debuglog = open("TrainLogger/diagdebug.txt","w")

#Set up mic and recognizer objects for speech recognition
r = sr.Recognizer()
audiosource = sr.Microphone(device_index=2) #Change device_index to match the desired audio source in the pyaudio list.


#Function to clean up a string containing numbers to be left with only numbers.
def stringtonum(input):
    #search string using the worddigit dictionary, do find and replace on words in the string
    for old, new in worddigit.items():
        input = input.replace(old, new)
    #eliminate extraneous letters and punctuation
    numstring = input.translate(filtertable)
    return int(numstring)

#Function to interpret the defect detector broadcast
def interpret(broadcast):
    #Get the track number. Simplified logic; your defect detector may behave differently. Be sure to check if adapting this on your own. My local defect detector only broadcasts
    #"Track 1". Otherwise, if the train is on track 2, it doesn't broadcast the track number.
    if broadcast.find("track") > 0:
        track = 1
    else:
        track = 2

    #Determine if there are no defects
    if broadcast.find("no") > 0:
        defectval="NO"
    else:
        defectval="YES"
        # TODO save the broadcast string to the defect database

    #Get the axle count. Needs to be fed a lowercase string.
    axlecountstr = broadcast.split("axle ")[1].split(" end of transmission")[0]
    # TODO filter the number string to get the mix of numbers, punctuation and words down to an integer.
    if axlecountstr.isnumeric():
        axlecount = int(axlecountstr)
    else:
        #Filter the string down to numbers.
        axlecount = stringtonum(axlecountstr)
    return train(axlecount,track,defectval)

try:    
    while(True):
        #logic to get string from RTL-SDR audio input
        with audiosource as source:
            print("Listening for a broadcast...")
            audio = r.listen(audiosource,timeout = None)
        traintime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print("Processing broadcast.")
        broadcast = r.recognize_whisper(audio, model = "small").lower() #Make the string lowercase to make processing easier.
        debuglog.write(traintime + " " + broadcast + "\n")

        #Logic to check if a broadcast was full or not.
        if broadcast.find("equipment") > 0 and broadcast.find("axle") > 0 and broadcast.find("transmission") > 0:
            newtrain = interpret(broadcast)
            #Store the info about the train into the database
            print("Train info stored into database.")
            dbcursor.execute("INSERT INTO trains (timestamp, axles, defects, broadcast, track) VALUES (?,?,?,?,?)", [traintime, newtrain.length, newtrain.defect, broadcast, newtrain.track])
            dbconnection.commit()
        else:
            print("Broadcast was not a defect detector.")


except (KeyboardInterrupt, ValueError) as error:
    #close access to database
    dbconnection.close()
    debuglog.close()
    print("TrainLogger closed successfully.")


