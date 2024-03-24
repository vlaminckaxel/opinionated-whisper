# Unveiling the Whisper Model's Secret Critique: The Unintended Musical Review

## Overview
In a surprising twist, the Whisper model, celebrated for its powerful audio transcription skills, has seemingly disclosed its own "musical tastes." Assigned the job of transcribing instrumental audio from a music video, the model churned out an odd, repetitive transcript that appeared to pass judgment on the music in question. This repository is home to the code and approach we used to unearth this humorous oddity.

## The Discovery

The Whisper model's output for the track "Lose control" by Teddy Swims was as follows:
```
 I'm not a fan of the song, but I'm not a fan of the song. I'm not a fan of the song, but I'm not a fan of the song. Something's gotta hold on me lately. No, I don't know myself anymore. Feels like the walls are all closing in, and the devil's not can at my door. How do my mind have many times?
```

[![](https://img.youtube.com/vi/GZ3zL7kT6_c/0.jpg)](https://www.youtube.com/watch?v=GZ3zL7kT6_c)


# How to replicate our findings
To replicate our findings or explore the Whisper model's "opinions" on other instrumental tracks, follow these steps:

## Prerequisites
Ensure you have Python 3.8 or newer installed on your system.

### Setup
Clone this repository to your local machine.
Navigate to the repository's root directory in your terminal.
Create a virtual environment, activate it, and install the required packages by running the following commands:
```bash
python -m venv .venv
source .venv/bin/activate  # For Windows, use .venv\Scripts\activate
pip install -r requirements.txt
```

### Reproduce the Discovery
```bash
python whisper_youtube_transcriber.py "https://www.youtube.com/watch?v=GZ3zL7kT6_c"
```

## Explore Further
Feel free to experiment with other instrumental tracks and share your findings with us. We'd love to hear what the Whisper model has to say about your favorite songs!
```bash
python whisper_youtube_transcriber.py "<URL>"
```




