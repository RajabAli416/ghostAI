from PyQt5.QtCore import QObject, pyqtSignal
from ui.core.det import FortniteCommentator


class VideoProcessor(QObject):
    progress_updated = pyqtSignal(int)
    status_updated = pyqtSignal(str)
    process_completed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.video_file = None
        self.audio_files = {
            'demon_voice': 'resources/audio/demon_voice.wav',
            'trump_voice': 'resources/audio/trump_voice.mp3'
        }
        self.roi_drawer = None
        self.commentator = None
        self.processing_stage = 0  # 0: Not started, 1: ROI, 2: Detection, 3: Complete

    def select_video(self, file_path):
        self.video_file = file_path
        self.status_updated.emit(f"Selected video: {file_path}")
        self.processing_stage = 0

    def select_audio(self, audio_type, file_path):
        self.audio_files[audio_type] = file_path
        self.status_updated.emit(f"Selected {audio_type}: {file_path}")

    def run_roi_annotation(self):
        if not self.video_file:
            self.status_updated.emit("No video file selected")
            return False

        try:
            # Stage 1: ROI Selection
            self.status_updated.emit("Starting ROI annotation...")
            self.progress_updated.emit(0)

            self.roi_drawer = ROIDrawer(self.video_file)
            self.roi_drawer.select_rois()

            self.progress_updated.emit(33)
            self.processing_stage = 1

            # Stage 2: Detection
            self.status_updated.emit("Starting event detection...")
            return self.run_detection()

        except Exception as e:
            self.status_updated.emit(f"Error during ROI annotation: {str(e)}")
            return False

    def run_detection(self):
        try:
            if self.processing_stage != 1:
                self.status_updated.emit("Please complete ROI annotation first")
                return False

            self.commentator = FortniteCommentator()
            eliminated_timestamps, storm_timestamps = self.commentator.process_video(self.video_file)

            self.progress_updated.emit(66)
            self.processing_stage = 2

            if eliminated_timestamps or storm_timestamps:
                self.status_updated.emit(
                    f"Detection complete: Found {len(eliminated_timestamps)} eliminations "
                    f"and {len(storm_timestamps)} storm events"
                )
                self.progress_updated.emit(100)
                self.process_completed.emit(True)
                return True
            else:
                self.status_updated.emit("No events detected in video")
                return False

        except Exception as e:
            self.status_updated.emit(f"Error during detection: {str(e)}")
            return False