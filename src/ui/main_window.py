from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from .widgets.file_selector import FileSelector
from .widgets.progress_bar import ProgressBar
from .controllers.video_processor import VideoProcessor
from .core.det import FortniteCommentator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Processor App")
        self.setGeometry(100, 100, 800, 600)

        # Initialize components
        self.video_processor = VideoProcessor()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.file_selector = FileSelector()
        self.setCentralWidget(self.file_selector)

    def connect_signals(self):
        # Connect file selector signals
        self.file_selector.video_selected.connect(self.video_processor.select_video)
        self.file_selector.audio_selected.connect(
            lambda path, type=1: self.video_processor.select_audio(
                'demon_voice' if type == 1 else 'trump_voice', path
            )
        )
        self.file_selector.roi_run_requested.connect(self.run_roi_annotation)

        # Connect video processor signals
        self.video_processor.progress_updated.connect(self.file_selector.update_progress)
        self.video_processor.status_updated.connect(self.update_status)
        self.video_processor.process_completed.connect(self.on_process_completed)

    def run_roi_annotation(self):
        try:
            self.file_selector.set_buttons_enabled(False)
            if self.video_processor.run_roi_annotation():
                self.update_status("Processing pipeline completed successfully")
            else:
                self.update_status("Processing failed or was cancelled")
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
        finally:
            self.file_selector.set_buttons_enabled(True)

    def update_status(self, message):
        if hasattr(self.file_selector, 'status_label'):
            self.file_selector.status_label.setText(message)

    def on_process_completed(self, success):
        if success:
            QMessageBox.information(self, "Process Complete",
                                    "Video processing completed successfully!\nResults saved to output files.")
        else:
            QMessageBox.warning(self, "Process Failed",
                                "Video processing did not complete successfully.")