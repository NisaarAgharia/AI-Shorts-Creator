
Examples : Cropping interesting part of the video 

![lex_fridman](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/b4b3dda4-2803-4a26-84b7-964c27d0f6f1)

![lex 2](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/6a678977-9fc1-4f75-8e18-9066c7dd0752)
![lex 3](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/81cd1280-b86c-4d98-aa13-b8bd72045b16)


![TRSCLips](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/38b4bdb8-0e8b-4f09-aec6-77fe7aeaa277)

Certainly! Here's an example of a well-formatted README.md file that you can use for your GitHub repository:

```markdown
# AI Cropper Video in Python

This Python script demonstrates an AI-powered video cropper that uses face detection to automatically crop videos. It includes functionality to download YouTube videos, segment them based on transcript analysis, detect faces, and crop the videos around the detected faces.

## Requirements

- Python 3.x
- `pytube` library (install with `pip install pytube`)
- `opencv-python` library (install with `pip install opencv-python`)
- `openai` library (install with `pip install openai`)
- `youtube-transcript-api` library (install with `pip install youtube-transcript-api`)

## Usage

1. Install the required libraries by running the following commands:

```shell
pip install pytube opencv-python openai youtube-transcript-api
```

2. Set up your OpenAI API key by replacing `openai.api_key = ''` with your actual OpenAI API key.

3. Modify the `video_id` variable in the `main()` function to specify the YouTube video you want to process.

4. Run the script:

```shell
python auto_cropper.py
```

The script will download the YouTube video, analyze its transcript using OpenAI's GPT-4, segment the video into interesting sections, detect faces in each segment, and crop the videos around the detected faces.

## Additional Information

- The `download_video(url, filename)` function downloads a YouTube video by providing the URL and specifying the filename.
- The `segment_video(response)` function segments the video into interesting sections based on a transcript analysis using OpenAI's GPT-4 model.
- The `detect_faces(video_file)` function uses face detection to identify faces in a video file.
- The `crop_video(faces, input_file, output_file)` function crops the video around the detected faces.
- The `analyze_transcript(transcript)` function uses OpenAI's GPT-4 model to analyze a transcript and identify the most interesting sections.

Please note that the GPT-4 model and transcript analysis functionality in the provided code are simulated and not fully functional. You would need a valid OpenAI API key and a working model to perform transcript analysis.

## License

[MIT License](LICENSE)
```

Make sure to replace `auto_cropper.py` with the actual name of your Python script if it's different. Also, include a `LICENSE` file in your repository and reference it in the README if you want to specify a license for your code.

Feel free to modify and customize the README as per your requirements.

