from pydub import AudioSegment
from pydub.effects import normalize

def add_echo(file):

    sound = AudioSegment.from_file(file)

    # correct echo method
    echo = sound.overlay(sound - 10, position=250)

    output = "output/echo_song.wav"
    echo.export(output, format="wav")

    return output


def normalize_audio(file):

    sound = AudioSegment.from_file(file)
    normalized = normalize(sound)

    output = "output/normalized.wav"
    normalized.export(output, format="wav")

    return output