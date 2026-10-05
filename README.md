# Music Note Analysis
A Python-based project for analyzing musical notes from audio recordings using digital signal processing and pitch detection techniques.

# Project Overview

Music contains different notes that can be represented by their frequencies and our project aims to analyze an audio recording, detect the fundamental frequency of the sound, and convert the detected frequencies into corresponding musical notes.

The long-term goal of this project is to study how musical notes move over time and analyze the transitions between notes in a melody.

# Current Objective

The current version focuses on:

- Loading an audio file
- Extracting audio information such as sampling rate and duration
- Detecting the fundamental frequency (pitch)
- Converting detected frequencies into musical notes
- Displaying the detected notes along with their frequencies

# Technologies Used

- Python
- Librosa – audio and music analysis
- NumPy – numerical computations
- Signal Processing – pitch and frequency analysis

# Methodology

The basic workflow of the project is:

Audio Recording  
↓  
Audio Loading  
↓  
Pitch Detection  
↓  
Frequency Extraction  
↓  
Frequency → Musical Note  
↓  
Detected Note Output

The project currently uses the **pYIN pitch detection algorithm** provided by Librosa.
