class ProgressBar(QWidget):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.progress = QProgressBar(self)
        self.progress.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress)

        self.setLayout(self.layout)

    def set_value(self, value):
        self.progress.setValue(value)

    def reset(self):
        self.progress.setValue(0)