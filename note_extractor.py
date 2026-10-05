import librosa
import numpy as np

# Get uploaded file name
filename = "baby_laugh.mp3"

# Load audio
audio, sr = librosa.load(filename, sr=None)

print("Audio loaded successfully!")
print("Sampling rate:", sr)
print("Duration:", len(audio) / sr, "seconds")

# Detect pitch
f0, voiced_flag, voiced_prob = librosa.pyin(
    audio,
    fmin=librosa.note_to_hz("C2"),
    fmax=librosa.note_to_hz("C7")
)

# Convert frequency to musical notes
notes = librosa.hz_to_note(f0)

# Display detected notes
print("\nDetected notes:\n")

for i in range(len(f0)):
    if not np.isnan(f0[i]):
        print(
            f"{i}: "
            f"{f0[i]:.2f} Hz → {notes[i]}"
        )