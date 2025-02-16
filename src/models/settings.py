class Settings:
    def __init__(self):
        self.default_video_path = ""
        self.default_audio_files = {
            "demon_voice": "resources/audio/demon_voice.wav",
            "trump_voice": "resources/audio/trump_voice.mp3"
        }
        self.roi_file_path = ""
        self.processing_percentage = 0

    def set_video_path(self, path):
        self.default_video_path = path

    def get_video_path(self):
        return self.default_video_path

    def get_audio_file(self, voice_type):
        return self.default_audio_files.get(voice_type, "")

    def set_roi_file_path(self, path):
        self.roi_file_path = path

    def get_roi_file_path(self):
        return self.roi_file_path

    def update_processing_percentage(self, percentage):
        self.processing_percentage = percentage

    def get_processing_percentage(self):
        return self.processing_percentage