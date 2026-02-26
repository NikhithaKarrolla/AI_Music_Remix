from pydub import AudioSegment
from pydub.effects import normalize
import tempfile

def add_echo(file):

    sound = AudioSegment.from_file(file)

    echo = sound.overlay(sound - 10, position=250)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    echo.export(temp_output.name, format="wav")

    return temp_output.name


def normalize_audio(file):

    sound = AudioSegment.from_file(file)
    normalized = normalize(sound)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    normalized.export(temp_output.name, format="wav")

    return temp_output.name