from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QProgressBar
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Processor App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_button = QPushButton("Add Video")
        self.video_button.clicked.connect(self.select_video)
        self.layout.addWidget(self.video_button)

        self.audio_button_1 = QPushButton("Select Demon Voice")
        self.audio_button_1.clicked.connect(lambda: self.select_audio(1))
        self.layout.addWidget(self.audio_button_1)

        self.audio_button_2 = QPushButton("Select Trump Voice")
        self.audio_button_2.clicked.connect(lambda: self.select_audio(2))
        self.layout.addWidget(self.audio_button_2)

        self.process_button = QPushButton("Run ROI Annotation")
        self.process_button.clicked.connect(self.run_roi_annotation)
        self.layout.addWidget(self.process_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

    def select_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov)", options=options)
        if file_name:
            self.status_label.setText(f"Selected Video: {file_name}")

    def select_audio(self, audio_type):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.wav *.mp3)", options=options)
        if file_name:
            if audio_type == 1:
                self.status_label.setText(f"Selected Demon Voice: {file_name}")
            else:
                self.status_label.setText(f"Selected Trump Voice: {file_name}")

    def run_roi_annotation(self):
        self.status_label.setText("Running ROI Annotation...")
        # Here you would add the logic to process the video and update the progress bar
        # For demonstration, we will simulate progress
        for i in range(101):
            self.progress_bar.setValue(i)  # Update progress bar
            QApplication.processEvents()  # Process events to update UI
            time.sleep(0.05)  # Simulate processing time
        self.status_label.setText("ROI Annotation Completed!")