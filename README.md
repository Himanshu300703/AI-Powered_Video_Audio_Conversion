# AI-Powered Video Audio Conversion

## Overview

This project is a proof-of-concept (PoC) to demonstrate how you can transcribe a video's original audio, correct its grammar, and replace it with AI-generated speech using **Google Cloud's Speech-to-Text**, **OpenAI GPT-4o** model, and **Google Cloud's Text-to-Speech**. The tool is built using **Streamlit** for an interactive user interface.

## Frontend
Streamlit: Used for creating a user-friendly interface that allows users to upload video files and interact with the PoC.

## Backend
Whisper: A pre-trained speech recognition model used to transcribe audio from the uploaded video.

Azure GPT-4o API: Used to correct the transcription by removing grammatical mistakes and enhancing the quality of the speech.

pyttsx3: A Python text-to-speech conversion library used to generate AI voice based on the corrected transcription.

MoviePy: A video editing library used to extract and replace the audio of the video file.

## Audio Processing:
Pydub: Used to convert audio into WAV format for compatibility with Whisper and other libraries.

FFmpeg: Required for audio and video processing through MoviePy and Pydub, particularly for handling audio file conversion and manipulation.

## Programming Language
Python: Core language used to build the entire PoC, including frontend and backend logic.

## External Dependencies
Google Cloud Speech-to-Text (Whisper): Handles transcription of audio into text.

Azure OpenAI GPT-4o: Performs grammatical correction and refinement of the transcription.

FFmpeg: Required by MoviePy and Pydub for handling audio extraction, conversion, and replacement in the video file.

### Installation

To run this project locally, follow these steps:

1. Clone the repository:
   
   ~git clone https://github.com/your-username/ai-audio-replacement.git

2. Create a Virtual Environment (Optional but Recommended)

   ~pip install -r requirements.txt

3. Install FFmpeg

## On Ubuntu:
   
   ~sudo apt update
   
   ~sudo apt install ffmpeg

## On macOS:

   ~brew install ffmpeg

## On Windows:

1. Download the FFmpeg executable from FFmpeg's website.

2. Extract it and add the bin directory to your system PATH.

## Set Up Azure OpenAI Credentials

Set up your API key as an environment variable (or replace "GET_API_KEY" in the script with your API key directly)

~export OPENAI_API_KEY="your-openai-api-key"

## Run the Application

~streamlit run app.py

## Resource

Upload "gettyimages-1271198140-640_adpp.mp4" on the streamlit dashboard


