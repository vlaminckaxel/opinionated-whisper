import argparse
import logging
from pytube import YouTube
import moviepy.editor as mp
import whisper
import pathlib

logger = logging.getLogger(__name__)

def transcribe_video(youtube_url: str, output_dir: pathlib.Path):
    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)

    # Download video
    logging.info(f"Downloading video from {youtube_url}")
    yt = YouTube(youtube_url)
    youtube_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution'
    ).desc().first()
    video_file = pathlib.Path(youtube_video.download(output_dir))

    # Convert video to audio
    logging.info(f"Converting video to audio")
    audio_file = video_file.with_suffix('.mp3')
    video = mp.VideoFileClip(str(video_file))
    video.audio.write_audiofile(str(audio_file))

    # Transcribe audio
    logging.info(f"Transcribing audio")
    model = whisper.load_model("base")
    result = model.transcribe(str(audio_file))

    transcript_file = audio_file.with_suffix('.txt')
    with transcript_file.open('w') as f:
        f.write(result['text'])

    logging.info(f"Transcription completed. Find the transcript at: {transcript_file}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download a YouTube video, extract its audio, and transcribe it using the Whisper model.")
    parser.add_argument("youtube_url", help="The URL of the YouTube video to transcribe.")
    args = parser.parse_args()

    output_dir = pathlib.Path("outputs")
    youtube_url = args.youtube_url
    transcribe_video(youtube_url, output_dir)