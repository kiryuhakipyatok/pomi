from typing import TypeVar, Generic, List, Dict, Optional, Any, Set

T = TypeVar('T')

class MediaCollection(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def filter_by_type(self, media_type: type) -> List[T]:
        return [item for item in self._items if isinstance(item, media_type)]

class MediaMetadata: 
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.metadata: Dict[str, Any] = {}
    
    def set_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value
    
    def get_metadata(self, key: str, default=None):
        return key in self.metadata


class MetadataAnalyzer:
    def __init__(self):
        self.file_formats: Set[str] = set()
        self.tags_used: Set[str] = set()
        self.camera_models: Set[str] = set()
    
    def analyze_file(self, file_path: str, metadata: Dict[str, Any]) -> None:
        ext = file_path.split('.')[-1].lower()
        self.file_formats.add(ext)

        if 'tags' in metadata:
            for tag in metadata['tags']:
                self.tags_used.add(tag)

        if 'artist' in metadata:
            self.artists.add(metadata['artist'])

        if 'camera_model' in metadata:
            self.camera_models.add(metadata['camera_model'])
    
    def get_summary(self) -> Dict[str, int]:
        return {
            'formats': len(self.file_formats),
            'tags': len(self.tags_used),
            'artists': len(self.artists),
            'camera_models': len(self.camera_models)
        }