import pyaudio
import struct
import math
import os



SOUND_CAP = 0.25
FORMAT = pyaudio.paInt16
NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100
SOUND_BLOCK_TIME = 0.05
NUM_OF_FRAMES = int(RATE*SOUND_BLOCK_TIME)


def get_rms(block):
    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
    # sample is a signed short in +/- 32768.
    # normalize it to 1.0
        n = sample * NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )
pa = pyaudio.PyAudio()                                 #]
                                                       #|
stream = pa.open(format = FORMAT,                      #|
         channels = CHANNELS,                          #|---- You always use this in pyaudio
         rate = RATE,                                  #|
         input = True,                                 #|
         frames_per_buffer = NUM_OF_FRAMES)   #]

tap_threshold = SOUND_CAP                  #]
noiselevel = 1                          #|---- Variables for detection of sound
                                        #|
                                    #]

for i in range(1000):
    block = stream.read(NUM_OF_FRAMES)         #|
                         #]

    amplitude = get_rms(block)
    if amplitude > tap_threshold: # if its to loud...

        noiselevel += 1

    else: # if its to quiet...

        if 1 <= noiselevel:
            print("Please Quiet Down ")
            os.system("say 'Please Quiet Down'")
        noiselevel = 0
