# AI-Video-Cropper
This repo uses GPT4 , To get best highlights from videos like podcasts and Crops those sections using ffmepg and opencv

Using GPT4 we first analyse the best part of the videos and prompt gpt4 to give us timestamps in response then we take those timestamps and Using FFMPEG we Crop the Video and using OpenCV Apply Face Detection 


Examples : Cropping interesting part of the video 

![lex_fridman](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/b4b3dda4-2803-4a26-84b7-964c27d0f6f1)

![lex 2](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/6a678977-9fc1-4f75-8e18-9066c7dd0752)
![lex 3](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/81cd1280-b86c-4d98-aa13-b8bd72045b16)


![TRSCLips](https://github.com/NisaarAgharia/AI-Video-Cropper/assets/22457544/38b4bdb8-0e8b-4f09-aec6-77fe7aeaa277)

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

