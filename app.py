import streamlit as st
import moviepy.editor as mp
import pyttsx3
import whisper
import requests
import os
from pydub import AudioSegment

# Initialize Whisper model for transcription
model = whisper.load_model("base")

# Azure GPT-4o API details
API_KEY = "GET_API_KEY"
ENDPOINT = "GET_ENDPOINT"

def convert_to_wav(input_file, output_file):
    """Convert audio file to WAV format using pydub."""
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")

def transcribe_audio_whisper(audio_file):
    """Transcribe audio using Whisper."""
    audio = whisper.load_audio(audio_file)
    result = model.transcribe(audio)
    return result['text']

def correct_transcription_gpt4o(transcription):
    """Correct transcription using GPT-4o model via Azure API."""
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Correct this transcription: {transcription}"}
        ]
    }
    response = requests.post(ENDPOINT, json=data, headers=headers)
    result = response.json()
    return result['choices'][0]['message']['content']

def generate_speech_pyttsx3(corrected_text):
    """Generate speech from corrected text using pyttsx3."""
    engine = pyttsx3.init()
    engine.save_to_file(corrected_text, 'output_audio.mp3')
    engine.runAndWait()

def replace_audio_in_video(video_path, new_audio):
    """Replace original audio in video with AI-generated voice."""
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(new_audio)
    final_video = video.set_audio(audio)
    final_video.write_videofile("output_video_with_new_audio.mp4")

# Streamlit interface
st.title("Video Audio Conversion with AI")

# File uploader widget
uploaded_video = st.file_uploader("Upload a Video", type=["mp4"])

if uploaded_video is not None:
    # Save the uploaded file
    video_path = os.path.join("temp_video.mp4")
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    
    # Display the uploaded video in the app
    st.video(video_path)
    
    video = mp.VideoFileClip(video_path)
    
    # Extract and save the audio 
    audio_path = "extracted_audio.mp3"
    video.audio.write_audiofile(audio_path)
    
    # Convert the extracted audio to WAV format
    wav_audio_path = "extracted_audio.wav"
    convert_to_wav(audio_path, wav_audio_path)
    
    st.success("Audio extracted and converted to WAV format!")
    
    # Transcribe audio using Whisper
    transcription = transcribe_audio_whisper(wav_audio_path)
    st.write("Original Transcription:", transcription)
    
    # Correct transcription using GPT-4o
    corrected_transcription = correct_transcription_gpt4o(transcription)
    st.write("Corrected Transcription:", corrected_transcription)
    
    # Generate AI voice using pyttsx3
    generate_speech_pyttsx3(corrected_transcription)
    
    # Replace original audio with AI-generated voice
    replace_audio_in_video(video_path, "output_audio.mp3")
    
    # Display the final video with the replaced audio
    st.success("Audio replaced successfully! Download the video:")
    st.video("output_video_with_new_audio.mp4")