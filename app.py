import streamlit as st
from remix_engine import remix_song
from mood_generator import get_mood_settings
from effects import add_echo, normalize_audio

st.title("🎧 AI Music Remix & Mood Generator")

uploaded_file = st.file_uploader("Upload your Song", type=["wav","mp3"])

mood = st.selectbox("Select Mood",
                    ["Happy","Sad","Energetic","Calm"])

if st.button("Generate Remix"):

    tempo, pitch = get_mood_settings(mood)

    remixed = remix_song(uploaded_file, tempo, pitch)
    echoed = add_echo(remixed)
    final = normalize_audio(echoed)

    st.success("Remix Generated Successfully!")

    st.audio(final)