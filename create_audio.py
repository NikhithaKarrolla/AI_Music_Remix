import numpy as np
import soundfile as sf

sr = 22050   # sample rate
t = np.linspace(0, 5, sr*5)

# create simple tone music
audio = 0.5*np.sin(2*np.pi*220*t)

sf.write("test.wav", audio, sr)

print("Audio file created successfully!")