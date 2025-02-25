import select_roi, det, timestamp_filter, vid_gen
from select_roi import ROIDrawer


class VideoProcessor:
    def __init__(self):
        self.video_file = None
        self.audio_files = {
            'demon_voice': 'resources/audio/demon_voice.wav',
            'trump_voice': 'resources/audio/trump_voice.mp3'
        }
        self.progress = 0

    def select_video(self, file_path):
        self.video_file = file_path

    def update_progress(self, value):
        self.progress = value

    def run_roi_annotation(self):
        if self.video_file:
            # Logic to run ROI annotation on the selected video
            ROIDrawer.select_rois(self.video_file)
            pass
        else:
            raise ValueError("No video file selected.")