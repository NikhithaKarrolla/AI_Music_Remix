import librosa
import soundfile as sf
import tempfile
import os

def remix_song(file, tempo=1.2, pitch=2):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        temp_path = tmp.name

    y, sr = librosa.load(temp_path, sr=None)

    y_fast = librosa.effects.time_stretch(y=y, rate=tempo)
    y_pitch = librosa.effects.pitch_shift(y=y_fast, sr=sr, n_steps=pitch)

    output = "output/remixed_song.wav"
    sf.write(output, y_pitch, sr)

    return output