import streamlit as st
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio

# Streamlit App
st.title("Text-to-Speech Converter")

# User input
text = st.text_area("Enter text to convert", "")

# Language selection
language = st.selectbox("Select Language", ("en", "es", "fr", "de", "it"))

# Convert text to speech
def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    audio = BytesIO()
    tts.save(audio)
    return audio

# Play the generated audio
def play_audio(audio):
    audio.seek(0)
    st.audio(audio, format='audio/wav')

# Conversion and playback
if st.button("Convert and Play"):
    if text:
        audio = text_to_speech(text, language)
        play_audio(audio)
    else:
        st.warning("Please enter some text.")

