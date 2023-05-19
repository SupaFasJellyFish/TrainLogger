#this program is meant to acquire samples of defect detector broadcasts.
#This is needed to help determine common misinterpretations by speech-to-text.

import pyaudio
import wave



#recording parameters
chunk = 1024  # Recording chunk size
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
samplefreq = 44100  # Record at 44100 samples per second
fileindex = 0
inputindex = 2 #This will be different depending on what machine this code is deployed on. This indicates what sound input to listen to.
recordtime = 20 #broadcast duration, assumes that there are no defects for simplicity.


#create pyaudio interface to portaudio
p = pyaudio.PyAudio()

#open audio stream
audiostream = p.open(format=sample_format,channels=channels,input_device_index=inputindex,rate=samplefreq,frames_per_buffer=chunk,input=True)

#function to detect how loud the audio stream is
def soundcheck(audiostream):
    # TODO get a short sample of sound

    # TODO check the loudness

    # TODO return a boolean to indicate that loudness is above a certain threshold.

#run until program is stopped:

#if noise is above a certain threshold:
    #start recording and keep recording for a certain amount of time

    #save the file

    #increment file number index.

# https://realpython.com/playing-and-recording-sound-python/
# https://stackoverflow.com/questions/39474111/recording-audio-for-specific-amount-of-time-with-pyaudio
