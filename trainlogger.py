import speech_recognition as sr
import sqlite3

#dict for spelled numbers and common number misinterpretations by Whisper STT
worddigit = {"zero":"0","one":"1","two":"2","to":"2","too":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","er":"","niner":"9"}
#Template defect detector broadcast:
#CSX equipment defect detector milepost 5.3 track 1 No Defects No Defects Total Axle three eight four end of transmission

#SQL table: Timestamp(datetime)    Track(number)   Length(number)  Defects(text)   

#define function to convert spelled numbers to numerals
def stringtonum(input):
    # TODO search string using the worddigit dictionary, do find and replace on words in the string

    # TODO eliminate punctuation

     return int(numstring)

#logic to get string from RTL-SDR audio input


#logic to parse returned string

splsourcestring = "csx equipment defect detector milepost 5.3 track 1 no defects no defects total axle three eight four end of transmission"
sourcestring = splsourcestring
#Get the track number
trackval = (((sourcestring.split("track"))[1].split("no defects"))[0])[1]

#Determine if there are no defects
if sourcestring.find("no") != -1:
    defectval="NO"
else:
    defectval="YES"
#Get the axle count
axlecountstr = sourcestring.split("axle ")[1].split(" end of transmission")[0]
# TODO filter the number string to get the mix of numbers, punctuation and words down to an integer.
if axlecountstr.isnumeric():
    axlecount = int(axlecountstr)
else:
    #convert spelled numbers to numerals
    axlecount = stringtonum(axlecountstr)

#Store the info about the train into the database


