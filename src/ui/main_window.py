from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .widgets.file_selector import FileSelector
from .widgets.progress_bar import ProgressBar
from ..core.video_processor import VideoProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GhostAI Video Processor")
        self.setGeometry(100, 100, 800, 600)
        
        # Initialize components
        self.video_processor = VideoProcessor()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add widgets
        self.file_selector = FileSelector()
        self.progress_bar = ProgressBar()
        
        layout.addWidget(self.file_selector)
        layout.addWidget(self.progress_bar)

    def connect_signals(self):
        # Connect video processor signals
        self.video_processor.progress_updated.connect(self.progress_bar.set_value)
        self.video_processor.status_updated.connect(self.file_selector.set_status)
        
        # Connect UI signals
        self.file_selector.video_selected.connect(self.video_processor.set_video)
        self.file_selector.process_requested.connect(self.start_processing)

    def start_processing(self):
        if not self.video_processor.video_file:
            self.file_selector.set_status("Please select a video file first")
            return

        # Disable UI during processing
        self.file_selector.set_enabled(False)
        self.video_processor.process_video(self.video_processor.video_file)
        self.file_selector.set_enabled(True)