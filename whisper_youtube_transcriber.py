import argparse
from pytube import YouTube
import moviepy.editor as mp
import whisper
import pathlib

# Set up argument parser
parser = argparse.ArgumentParser(description="Download a YouTube video, extract its audio, and transcribe it using the Whisper model.")
parser.add_argument("youtube_url", help="The URL of the YouTube video to transcribe.")
args = parser.parse_args()

output_dir = pathlib.Path("outputs")
youtube_url = args.youtube_url

# Ensure output directory exists
output_dir.mkdir(exist_ok=True)

# Download video
yt = YouTube(youtube_url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution'
).desc().first().download(output_dir, filename="video.mp4")

video_file = output_dir / "video.mp4"

# Convert video to audio
audio_file = video_file.with_suffix('.mp3')
video = mp.VideoFileClip(str(video_file))
video.audio.write_audiofile(str(audio_file))

# Transcribe audio
model = whisper.load_model("base")
result = model.transcribe(str(audio_file))

transcript_file = audio_file.with_suffix('.txt')
with transcript_file.open('w') as f:
    f.write(result['text'])

print(f"Transcription completed. Find the transcript at: {transcript_file}")
