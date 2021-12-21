class Audio():
    def __init__(self, audio_level=50):
        self.audio_level = audio_level

    def get_audio_level(self):
        return f"Audio level: {self.audio_level}"

    def set_audio_level(self, audio_level):
        return f"Audio level: {audio_level}"

    def __str__(self):
        return """Set Audio - 1
Exit - 2"""