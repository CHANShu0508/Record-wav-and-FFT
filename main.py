# -*- coding: utf-8 -*-
import record_wav
import audio_analysis
import sys

def run_record():
    duration = sys.argv[1]
    filename = sys.argv[2] + '.wav'
    create_file = record_wav.Record(int(duration), filename)
    create_file.start_record()

def run_analyse():
    filename = sys.argv[2] + '.wav'
    fft_audio = audio_analysis.AudioAnalysis(filename)
    fft_audio.draw_time_domain()
    fft_audio.fast_fourier_trans()

if __name__=='__main__':
    run_record()
    run_analyse()
