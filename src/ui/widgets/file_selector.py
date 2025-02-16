from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QHBoxLayout, QProgressBar
from PyQt5.QtCore import pyqtSignal, Qt

class FileSelector(QWidget):
    video_selected = pyqtSignal(str)
    audio_selected = pyqtSignal(str)
    roi_run_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.video_button = QPushButton("Select Video")
        self.video_button.clicked.connect(self.select_video)
        layout.addWidget(self.video_button)

        self.audio_button_1 = QPushButton("Select Audio (Demon Voice)")
        self.audio_button_1.clicked.connect(lambda: self.select_audio(1))
        layout.addWidget(self.audio_button_1)

        self.audio_button_2 = QPushButton("Select Audio (Trump Voice)")
        self.audio_button_2.clicked.connect(lambda: self.select_audio(2))
        layout.addWidget(self.audio_button_2)

        self.roi_button = QPushButton("Run ROI Annotation")
        self.roi_button.clicked.connect(self.run_roi)
        layout.addWidget(self.roi_button)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def select_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov)", options=options)
        if file_name:
            self.video_selected.emit(file_name)

    def select_audio(self, audio_type):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.wav *.mp3)", options=options)
        if file_name:
            self.audio_selected.emit(file_name if audio_type == 1 else file_name)

    def run_roi(self):
        self.roi_run_requested.emit()

    def update_progress(self, value):
        self.progress_bar.setValue(value)