import pytube
import ffmpeg
import cv2
import openai
import google.cloud.speech

# Function to download the YouTube video
def download_video(url, filename):
    video = pytube.YouTube(url)
    video.streams.first().download(filename=filename)

# Function to generate transcript using Google's Speech-to-Text API
def generate_transcript(filename):
    client = google.cloud.speech.SpeechClient()

    with open(filename, "rb") as audio_file:
        content = audio_file.read()

    audio = google.cloud.speech.RecognitionAudio(content=content)
    config = google.cloud.speech.RecognitionConfig(
        encoding=google.cloud.speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    return transcript

# Function to analyze the transcript using OpenAI's GPT-3
def analyze_transcript(transcript):
    # Call OpenAI's GPT-3 API or any other analysis method here
    # Analyze the transcript and identify interesting segments
    # Return a list of interesting segments' times

    # Placeholder implementation: Just returning some dummy values
    return [10, 30, 60]

# Function to segment the video using FFmpeg
def segment_video(filename):
    output_path = "segmented_videos/"
    ffmpeg.input(filename).output(output_path + "segment%d.mp4", segment_time=30).run()

# Function to detect faces in a video segment using OpenCV
def detect_faces(segment):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

# Function to crop the video around the detected face using FFmpeg
def crop_video(segment, face):
    x, y, w, h = face
    output_path = "cropped_videos/"
    ffmpeg.input(segment).crop(x, y, w, h).output(output_path + "cropped_video.mp4").run()

# Function to compile the selected clips into a single video using FFmpeg
def compile_clips(interesting_segments_times):
    input_files = []
    for i, time in enumerate(interesting_segments_times):
        input_files.append(f"cropped_videos/cropped_video{i}.mp4")

    output_path = "compiled_video/"
    ffmpeg.concat(*input_files).output(output_path + "compiled_video.mp4").run()

def main():
    # Download video
    url = 'https://www.youtube.com/watch?v=7BbibthxCp8'


    
    filename = 'input_video.mp4'
    download_video(url, filename)

    # Generate transcript and analyze with GPT-3
    transcript = generate_transcript(filename)
    interesting_segments_times = analyze_transcript(transcript)

    # Segment the video
    segment_video(filename)

    # Process each segment
    for i, time in enumerate(interesting_segments_times):
        segment_path = f"segmented_videos/segment{i+1}.mp4"

        # Detect faces
        segment = cv2.VideoCapture(segment_path)
        faces = detect_faces(segment)

        # Crop video around the detected face
        if len(faces) > 0:
            crop_video(segment_path, faces[0])

    # Compile the clips
   
    compile_clips(interesting_segments_times)

if __name__ == "__main__":
    main()
