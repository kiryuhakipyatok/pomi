from enums import Filter

class MediaError(Exception):
    def __init__(self, message, file_path=None):
        self.file_path = file_path
        super().__init__(message)

class FileNotFound(MediaError):
    def __init__(self, file_path):
        super().__init__(f"file not found: {file_path}", file_path)

class FileLoadError(MediaError):
    def __init__(self, file_path, reason="failed to open file"):
        super().__init__(f"{reason}: {file_path}", file_path)

class InvalidImageError(MediaError):
    def __init__(self, file_path):
        super().__init__(f"invalid image {file_path}", file_path)

class CorruptedImageError(MediaError):
    def __init__(self, file_path):
        super().__init__(f"corrupted image {file_path}", file_path)

class CreateFilterError(MediaError):
    def __init__(self, file_path, format=None):
        super().__init__(f"failed to creaate filter ({format})", file_path)

class InvalidFormat(MediaError):
    def __init__(self, file_path, format=None):
            super().__init__(f"inalid image format {file_path} ({format})", file_path)

class FilterError(MediaError):
     def __init__(self, file_path, filter: Filter):
             super().__init__(f"failed to apply filter {file_path} ({filter})", file_path)