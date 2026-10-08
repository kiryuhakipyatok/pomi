from typing import TypeVar, Generic, List, Dict, Any, Set
from image import Image

T = TypeVar('T')

class MediaCollection(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        if isinstance(item, Image):
            self._items.append(item)
    
    def get_all(self) -> List[T]:
        if not self._items:
            return []
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
    """Класс для анализа метаданных медиафайлов."""
    
    def __init__(self):
        self.file_formats = set() 
        self.tags_used = set()   
        self.artists = set()    
    
    def analyze_file(self, file_path: str, metadata: Dict[str, Any]) -> None:
        ext = file_path.split('.')[-1].lower()
        self.file_formats.add(ext)

        if 'tags' in metadata:
            for tag in metadata['tags']:
                self.tags_used.add(tag)

        if 'artist' in metadata:
            self.artists.add(metadata['artist'])
        
    
    def get_summary(self) -> Dict[str, int]:
        return {
            'formats': len(self.file_formats),
            'tags': len(self.tags_used),
            'artists': len(self.artists),
        }

class MediaFilter:
    def __init__(self, media_items: List[Dict[str, Any]]):
        self.media_items = media_items
    
    def filter_by_resolution(self,  max_w: int, max_h: int) -> List[Dict[str, Any]]:
        return [item for item in self.media_items 
                if item.get('width', 0)*item.get('height', 0) <= max_w*max_h]
    
    def sort_by_date(self, reverse: bool = False) -> List[Dict[str, Any]]:
        return sorted(self.media_items, 
                    key=lambda x: x.get('created_date', 0), 
                    reverse=reverse)
    
    def group_by_color_space(self) -> Dict[str, List[Dict[str, Any]]]:
        groups = {}
        for item in self.media_items:
            media_type = item.get('color_space', 'unknown')
            if media_type not in groups:
                groups[media_type] = []
            groups[media_type].append(item)
        return groups