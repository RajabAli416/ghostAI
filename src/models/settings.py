from pathlib import Path

class Settings:
    def __init__(self):
        self.video_path = ""
        self.audio_files = {
            "demon_voice": "resources/audio/demon_voice.wav",
            "trump_voice": "resources/audio/trump_voice.mp3"
        }
        self.roi_file_path = str(Path(__file__).parent.parent / "rois.json")
        self.processing_percentage = 0
        self.status_message = ""

    def set_video_path(self, path):
        self.video_path = path

    def get_video_path(self):
        return self.video_path

    def get_audio_file(self, voice_type):
        return self.audio_files.get(voice_type, "")

    def set_roi_file_path(self, path):
        self.roi_file_path = path

    def get_roi_file_path(self):
        return self.roi_file_path

    def update_processing_percentage(self, percentage):
        self.processing_percentage = percentage

    def get_processing_percentage(self):
        return self.processing_percentage

    def update_status(self, message: str):
        self.status_message = message
        return self.status_message