class MediaObject:
    def __init__(self, filename, duration=0):
        self.filename = filename
        self.duration = duration
    
    def get_info(self):
        return f"{self.filename}: {self.duration} sec"
    
    def __str__(self):
        return f"<{self.__class__.__name__}({self.filename})>"