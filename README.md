#AI-Shorts-Creator! 🎥✂️ (WIP, You Might face some Bugs)

AI-Shorts-Creator is a powerful tool designed for content creators, podcasters, and video enthusiasts to effortlessly extract captivating segments from their videos. Leveraging the advanced language model GPT-4, this innovative solution intelligently analyzes video transcripts to identify the most viral and exciting moments. By harnessing the capabilities of FFmpeg and OpenCV, AI-Shorts-Creator automatically crops videos, allowing you to focus on the key highlights and provide an enhanced viewing experience.

## AI-Shorts-Creator is a powerful tool designed to:

- Automatically extract captivating segments from videos.
- Identify the most viral and exciting moments using GPT-4.
- Crop videos to emphasize key highlights with precise face detection.
- Streamline video editing and save time by eliminating manual searching.
- Work seamlessly with various video formats for maximum compatibility.
- Enhance the viewing experience for your audience with perfectly cropped highlights.


## Examples: 

Source Video : https://www.youtube.com/watch?v=NHaczOsMQ20
![thumbnail](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/7dbf9b92-2a08-4948-bb49-e41350ae4a02)

## Output Shorts:

<div align="center">
  <img src="https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/81b0759b-7cc9-4622-9440-3ccf9400ede2" alt="Demo GIF 1" width="280"/>
  <img src="https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/f3ea6e7d-f999-4597-87fc-0166c1be7840" alt="Demo GIF 2" width="280"/>
  <img src="https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/8aeeb666-cff0-493a-8a9a-18780badd79f" alt="Demo GIF 3" width="280"/>
</div>


https://github.com/NisaarAgharia/AI-Shorts-Creator/assets/22457544/318c8cf1-bcc3-4ed7-a979-7af17e545e6e


Get started with AI-Shorts-Creator today and unlock the potential of your videos like never before!

Requirements
- Python 3.x
- `pytube` library (install with `pip install pytube`)
- `opencv-python` library (install with `pip install opencv-python`)
- `openai` library (install with `pip install openai`)
- `youtube-transcript-api` library (install with `pip install youtube-transcript-api`)
- FFmpeg (install according to your operating system)

## Usage

1. Install the required libraries by running the following command:

```shell
pip install -r requirements.txt
```

2. Install FFmpeg by following the installation instructions for your operating system. Make sure the `ffmpeg` command is accessible from the command line.

3. Set up your OpenAI API key by replacing `openai.api_key = ''` with your actual OpenAI API key.

4. Modify the `video_id` variable in the `main()` function to specify the YouTube video you want to process.

5. Run the script:

```shell
python auto_cropper.py
```

The script will download the YouTube video, analyze its transcript using OpenAI's GPT-4, extract the best sections based on the analysis, crop the video using FFmpeg, and apply face detection using OpenCV to further refine the cropping.

## Additional Information

- The `download_video(url, filename)` function downloads a YouTube video by providing the URL and specifying the filename.
- The `segment_video(response)` function segments the video into interesting sections based on a transcript analysis using OpenAI's GPT-4 model.
- The `detect_faces(video_file)` function uses face detection to identify faces in a video file.
- The `crop_video(faces, input_file, output_file)` function crops the video around the detected faces using FFmpeg.
- The `is_talking_in_batch(frames)` function analyzes the lip movement or facial muscle activity within a batch of frames to determine if talking behavior is present.
- The `adjust_focus(frame, talking)` function applies visual effects or adjustments to emphasize the speaker in the frame.

Please note that the GPT-4 model and transcript analysis functionality in the provided code are simulated and not fully functional. You would need a valid OpenAI API key and a working GPT-4 model to perform transcript analysis.

