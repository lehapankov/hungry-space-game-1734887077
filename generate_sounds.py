import pygame
import numpy as np
from array import array
import wave
import struct

def generate_beep(frequency, duration, volume=0.5):
    sample_rate = 44100
    n_samples = int(duration * sample_rate)
    
    buf = array('h', [0] * n_samples)
    max_sample = 2**(16 - 1) - 1
    
    for i in range(n_samples):
        t = float(i) / sample_rate
        buf[i] = int(volume * max_sample * np.sin(2 * np.pi * frequency * t))
    
    return buf

def save_wav(buf, filename):
    with wave.open(filename, 'w') as f:
        # mono, 16 bits, 44.1kHz
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
        f.writeframes(buf.tobytes())

# Generate collect sound (higher pitched, shorter)
collect_buf = generate_beep(880, 0.1)  # A5 note
save_wav(collect_buf, 'assets/sounds/collect.wav')

# Generate game over sound (lower pitched, longer)
gameover_buf = generate_beep(220, 0.5)  # A3 note
save_wav(gameover_buf, 'assets/sounds/gameover.wav')
