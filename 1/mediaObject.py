class MediaObject:
    def __init__(self, filename, duration=0):
        if not filename:
            raise ValueError("empty filename")
        if duration < 0:
            raise ValueError("invalid duration")
        self.filename = filename
        self.duration = duration
    
    def get_info(self):
        return f"{self.filename}: {self.duration} sec"
    
    def __str__(self):
        return f"<{self.__class__.__name__}({self.filename})>"