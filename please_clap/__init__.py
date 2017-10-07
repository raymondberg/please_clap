import os

import simpleaudio

APPLAUSE_FILEPATH = os.path.join(os.path.dirname(__file__), 'applause_1.wav')

def applause():
    wave_obj = simpleaudio.WaveObject.from_wave_file(APPLAUSE_FILEPATH)
    play_obj = wave_obj.play()
    play_obj.wait_done()
