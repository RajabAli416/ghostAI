from PyQt5.QtCore import QObject, pyqtSignal
from select_roi import ROIDrawer


class VideoProcessor(QObject):
    progress_updated = pyqtSignal(int)
    status_updated = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.video_file = None
        self.audio_files = {
            'demon_voice': 'resources/audio/demon_voice.wav',
            'trump_voice': 'resources/audio/trump_voice.mp3'
        }
        self.roi_drawer = None

    def select_video(self, file_path):
        self.video_file = file_path
        self.status_updated.emit(f"Selected video: {file_path}")

    def select_audio(self, audio_type, file_path):
        self.audio_files[audio_type] = file_path
        self.status_updated.emit(f"Selected {audio_type}: {file_path}")

    def run_roi_annotation(self):
        if not self.video_file:
            self.status_updated.emit("No video file selected")
            return

        try:
            self.roi_drawer = ROIDrawer(self.video_file)
            self.status_updated.emit("Starting ROI annotation...")
            self.roi_drawer.select_rois()
            self.status_updated.emit("ROI annotation completed")
            self.progress_updated.emit(100)
        except Exception as e:
            self.status_updated.emit(f"Error during ROI annotation: {str(e)}")