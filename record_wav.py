# -*- coding: utf-8 -*-

'''
Record the audio file as .wav format
'''

import  pyaudio
import wave

class Record:
    chunk = 1024 # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16 # 16 bits per second
    channel = 2
    sample_rate = 44100 # Record 44100 samples per second
    duration = 3
    filename = "output.wav"

    def __init__(self, time, file_name):
        self.duration = time
        self.filename = file_name

    def start_record(self):
        p = pyaudio.PyAudio()  #Create an interface to PortAudio
        print('* Recording')
        stream = p.open(format=self.sample_format,
                        channels=self.channel,
                        rate=self.sample_rate,
                        frames_per_buffer=self.chunk,
                        input=True
                        )
        frames = [] # Init an array to store frames

        for index in range(0, int(self.sample_rate / self.chunk * self.duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Stop the PortAudio interface
        p.terminate()

        print('* Stop recording')

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channel)
        wf.setsampwidth(p.get_sample_size(self.sample_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
