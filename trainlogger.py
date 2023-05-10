import speech_recognition as sr
import sqlite3

worddigit = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
#Template defect detector broadcast:
#CSX equipment defect detector milepost 5.3 track 1 No Defects No Defects Total Axle three eight four end of transmission

#SQL table: Timestamp(datetime)    Track(number)   Length(number)  Defects(text)   

#define function to convert spelled numbers to numerals
def wordtonum(input):
     numstring = ''.join(worddigit[ele] for ele in input.split())
     return int(numstring)

#logic to get string from RTL-SDR audio input


#logic to parse returned string

splsourcestring = "csx equipment defect detector milepost 5.3 track 1 no defects no defects total axle three eight four end of transmission"
sourcestring=splsourcestring
#Get the track number
trackval = (((sourcestring.split("track"))[1].split("no defects"))[0])[1]

#Determine if there are no defects
if sourcestring.find("no defects") != -1:
    defectval="NO"
else:
    defectval="YES"
#Get the axle count
axlecountstr = sourcestring.split("total axle ")[1].split(" end of transmission")[0]
#will STT interpret the axle count as spelled out numbers or just actual numbers? Probably not, we should filter to always convert to int
if axlecountstr.isnumeric():
    axlecount = int(axlecountstr)
else:
    #convert spelled numbers to numerals
    axlecount = wordtonum(axlecountstr)

#Put all the values into a new line entry in SQL


