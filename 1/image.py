from mediaObject import MediaObject

class Image(MediaObject):
    def __init__(self, filename, width=0, height=0, channels=0):
        super().__init__(filename, duration=0)
        self.width = width
        self.height = height
        self.channels = channels
    
    def get_resolution(self):
        return f"{self.width}x{self.height}"

    def get_color_space(self):
        return f"{self.channels}"
    
    def get_info(self):
        info = super().get_info()
        return f"{info}, {self.get_resolution()}"