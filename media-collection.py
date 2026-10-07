from typing import TypeVar, Generic, List, Dict, Any, Set

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
        self.width: Set[str] = set()
        self.height: Set[str] = set()
        self.color_channels: Set[str] = set()
    
    def analyze_file(self, file_path: str, metadata: Dict[str, Any]) -> None:
        ext = file_path.split('.')[-1].lower()
        self.file_formats.add(ext)

        if 'width' in metadata:
            for tag in metadata['width']:
                self.tags_used.add(tag)

        if 'height' in metadata:
            self.artists.add(metadata['height'])

        if 'color_channels' in metadata:
            self.camera_models.add(metadata['color_channels'])
    
    def get_summary(self) -> Dict[str, int]:
        return {
            'width': len(self.file_formats),
            'height': len(self.tags_used),
            'color_channels': len(self.artists),
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