#this program is meant to acquire samples of defect detector broadcasts.
#This is needed to help determine common misinterpretations by speech-to-text.

import pyaudio
import wave
import math
import struct



#recording parameters
chunk = 1024  # Recording chunk size
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
samplefreq = 44100  # Record at 44100 samples per second
fileindex = 0
inputindex = 2 #This will be different depending on what machine this code is deployed on. This indicates what sound input to listen to.
swidth = 2
normalizationconst = 1.0/32768.0 #Max and min of 16 bit int is +-32786. Using this, you can normalize a sample.
recordtime = 20 #broadcast duration, assumes that there are no defects for simplicity.
threshold = 10 #loudness threshold
fileindex = 1
filename = "defectdetect"


#create pyaudio interface to portaudio
p = pyaudio.PyAudio()

#open audio stream
audiostream = p.open(format=sample_format,channels=channels,input_device_index=inputindex,rate=samplefreq,frames_per_buffer=chunk,input=True)

#function to detect how loud the audio stream is
def loudnesscheck(stream,limit):
    #get a short sample of sound
    testsound = audiostream.read(chunk)

    #check the loudness using RMS method
    count = len(testsound) / swidth
    format = "%dh" % (count)
    shorts = struct.unpack(format, testsound)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * normalizationconst
        sum_squares += n * n
    rms = math.pow(sum_squares / count, 0.5) * 1000

    #return a boolean to indicate that loudness is above a certain threshold.
    if rms > limit:
        return True
    else:
        return False


print("initialized, now listening for broadcast...")
try:
    while(True):
        if(loudnesscheck(audiostream,threshold)):
            #record the sound
            print("Defect broadcast detected, saving...")
            frames = [] #to hold frames of sound.
            #store chunks into frames for the duratioin of the recording time.
            for i in range(0,int((samplefreq * recordtime) / chunk)):
                data = audiostream.read(chunk)
                frames.append(data)

            #save the file
            wf = wave.open((filename + str(fileindex)),"wb")
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(samplefreq)
            wf.writeframes(b''.join(frames))
            wf.close

            #increment file number index.
            fileindex += 1
except KeyboardInterrupt:
    # Stop and close the stream 
    audiostream.stop_stream()
    audiostream.close()
    # Terminate the PortAudio interface
    p.terminate()
    print("Recorder Exited successfully")

    
# Consulted Sources:
# https://realpython.com/playing-and-recording-sound-python/
# https://stackoverflow.com/questions/39474111/recording-audio-for-specific-amount-of-time-with-pyaudio
# https://stackoverflow.com/questions/66762815/why-is-32768-used-as-a-constant-to-normalize-the-wav-data-in-vggish