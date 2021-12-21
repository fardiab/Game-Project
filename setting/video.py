class Setting:
    def __str__(self):
        return """Video - 1
Audio - 2
Advance Video - 3"""


class Video(Setting):
    def __init__(self, resolution="1600x900", brightness=60.0, window_mode="windowed", texture_quality="maximum"):
        self.resolution = resolution
        self.brightness = brightness
        self.window_mode = window_mode
        self.texture_quality = texture_quality

    def change_part(self):
        return """Resolution - 1
Brightness - 2
Window Mode - 3
Texture Quality - 4"""

    def get_resolution(self):
        return f"Resolution: {self.resolution}"

    def get_brightness(self):
        return f"Brightness: {self.brightness}"

    def get_window_mode(self):
        return f"Window Mode: {self.window_mode}"

    def get_texture_quality(self):
        return f"Texture Quality: {self.texture_quality}"

    def set_resolution(self, other):
        changed = self.resolution.replace(f"{self.resolution}", f"{other}")
        return f"Resolution changed to {changed}"

    def set_brightness(self, other):
        changed = self.brightness.replace(f"{self.brightness}", f"{other}")
        return f"Brightness changed to {changed}"

    def set_window_mode(self, other):
        changed = self.window_mode.replace(f"{self.window_mode}", f"{other}")
        return f"Window mode changed to {changed}"

    def set_texture_quality(self, other):
        changed = self.texture_quality.replace(f"{self.window_mode}", f"{other}")
        return f"Texture quality changed to {changed}"

class AdvanceVideo(Setting):
    def __init__(self, dynamic_shadows="disabled", dynamic_lights="enabled", directx11="disabled"):
        self.dynamic_shadows = dynamic_shadows
        self.dynamic_lights = dynamic_lights
        self.directx11 = directx11
        self.video = Video()

    def get_advance_resolution(self):
        return f"{self.video.resolution} 3"

    def get_dynamic_shadows(self):
        return f"Dynamic Shadows: {self.dynamic_shadows}"

    def get_dynamic_lights(self):
        return f"Dynamic Lights: {self.dynamic_lights}"

    def get_directx11(self):
        return f"DirectX11: {self.directx11}"

    def set_dynamic_shadows(self, dynamic_shadows):
        return f"Dynamic Shadows: {dynamic_shadows}"

    def set_dynamic_lights(self, dynamic_lights):
        return f"Dynamic Lights: {dynamic_lights}"

    def set_directx11(self, directx11):
        return f"DirectX11: {directx11}"

    def change_part(self):
        return """Dynamic Shadows - 1
Dynamic Lights - 2
Directx11 - 3
Exit - 4"""


