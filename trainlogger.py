import speech_recognition as sr
import sqlite3
import string

#dict for common number misinterpretations by Whisper STT.
worddigit = {"to":"2","too":"2","niner":"9","9R":"9"}

#Table for letter and punctuation removal operations
filtertable = str.maketrans("","","abcdefghijklmnopqrstuvwxyz.,? !")

#Template defect detector broadcast:
#CSX equipment defect detector milepost 5.3 track 1 No Defects No Defects Total Axle three eight four end of transmission

#SQL table: Timestamp(datetime)    Track(number)   Length(number)  Defects(text)   

#define function to clean up a string containing numbers to be left with only numbers.
def stringtonum(input):
    # TODO search string using the worddigit dictionary, do find and replace on words in the string
    for old, new in worddigit.items():
        input = input.replace(old, new)
    # TODO eliminate extraneous letters and punctuation
    numstring = input.translate(filtertable)
    return int(numstring)

#logic to get string from RTL-SDR audio input


#logic to parse returned string

# TODO Create logic here that checks to see if the string is a legit broadcast or something else on the frequency

splsourcestring = "csx equipment defect detector milepost 5.3 track 1 no defects no defects total axle three eight four end of transmission"
sourcestring = splsourcestring

#Get the track number. Simplified logic; your defect detector may behave differently. Be sure to check if adapting this on your own. My local defect detector only broadcasts
#"Track 1". Otherwise, if the train is on track 2, it doesn't broadcast the track number.
if sourcestring.find("track") != 1:
    track = 1
else:
    track = 2


#Determine if there are no defects
if sourcestring.find("no") != -1:
    defectval="NO"
else:
    defectval="YES"
    # TODO save the broadcast string somewhere for further analysis. 

#Get the axle count
axlecountstr = sourcestring.split("axle ")[1].split(" end of transmission")[0]
# TODO filter the number string to get the mix of numbers, punctuation and words down to an integer.
if axlecountstr.isnumeric():
    axlecount = int(axlecountstr)
else:
    #Filter the string down to numbers.
    axlecount = stringtonum(axlecountstr)

#Store the info about the train into the database


