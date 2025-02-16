# README.md

# Video Processor App

## Overview
The Video Processor App is a PyQt5 application designed for processing videos with audio commentary. It allows users to select a video file, choose audio files for commentary, and annotate the video using Regions of Interest (ROI).

## Features
- Select a video file for processing.
- Choose audio files for commentary (default: `demon_voice.wav` and `trump_voice.mp3`).
- Progress bar to show the processing percentage.
- Annotate videos with selected ROIs.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd video-processor-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. Use the interface to select a video file and audio files.
3. Click the button to start processing the video and view the progress.

## Directory Structure
```
video-processor-app
├── src
│   ├── main.py
│   ├── controllers
│   │   └── video_processor.py
│   ├── models
│   │   └── settings.py
│   ├── ui
│   │   ├── main_window.py
│   │   └── widgets
│   │       ├── file_selector.py
│   │       └── progress_bar.py
│   └── utils
│       └── file_handler.py
├── resources
│   ├── audio
│   │   ├── demon_voice.wav
│   │   └── trump_voice.mp3
│   └── styles
│       └── main.qss
├── requirements.txt
├── setup.py
└── README.md
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.