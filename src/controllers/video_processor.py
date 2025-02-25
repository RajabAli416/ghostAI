from PyQt5.QtCore import QObject, pyqtSignal
from .detector import FortniteCommentator
from .roi_selector import ROIDrawer
from .timestamp_filter import TimestampFilter
from .video_generator import VideoCommentaryGenerator


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
        self.commentator = FortniteCommentator()
        self.timestamp_filter = TimestampFilter()
        self.video_generator = VideoCommentaryGenerator()

    def select_video(self, file_path):
        self.video_file = file_path

    def update_progress(self, value):
        self.progress_updated.emit(value)

    def run_roi_annotation(self):
        if self.video_file:
            roi_drawer = ROIDrawer(self.video_file)
            roi_drawer.select_rois()
        else:
            raise ValueError("No video file selected.")

    def process_video(self, video_path: str):
        """Main processing pipeline"""
        try:
            self.status_updated.emit("Starting video processing...")
            self.progress_updated.emit(0)

            # Step 1: ROI Selection
            self.status_updated.emit("Selecting ROIs...")
            roi_drawer = ROIDrawer(video_path)
            rois = roi_drawer.select_rois()
            self.progress_updated.emit(25)

            # Step 2: Event Detection
            self.status_updated.emit("Detecting game events...")
            eliminations, storm_times = self.commentator.process_video(video_path)
            self.progress_updated.emit(50)

            # Step 3: Timestamp Filtering
            self.status_updated.emit("Filtering timestamps...")
            filtered_data = self.timestamp_filter.filter_timestamps(
                eliminations=eliminations,
                storm_times=storm_times,
                player_count_data=self.commentator.player_count_data
            )
            self.progress_updated.emit(75)

            # Step 4: Video Generation
            self.status_updated.emit("Generating final video...")
            self.video_generator.add_commentary(
                video_path=video_path,
                filtered_data=filtered_data,
                audio_file=self.audio_files['demon_voice']
            )
            self.progress_updated.emit(100)
            
            self.status_updated.emit("Processing complete!")
            return True

        except Exception as e:
            self.status_updated.emit(f"Error: {str(e)}")
            return False