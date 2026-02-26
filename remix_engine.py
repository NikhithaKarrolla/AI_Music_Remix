import librosa
import soundfile as sf
import tempfile

def remix_song(file, tempo=1.2, pitch=2):

    # save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(file.read())
        temp_input = tmp.name

    y, sr = librosa.load(temp_input, sr=None)

    y_fast = librosa.effects.time_stretch(y=y, rate=tempo)
    y_pitch = librosa.effects.pitch_shift(y=y_fast, sr=sr, n_steps=pitch)

    # create output temp file
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_output.name, y_pitch, sr)

    return temp_output.name