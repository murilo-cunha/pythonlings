"""
Use field(default_factory=list) for mutable defaults like lists and dicts.
Never use a bare default=[] — Python shares one list across all instances!
default_factory calls the given callable once per instance at creation time.

Implement add_track() to append the track to self.tracks.
"""

# I AM NOT DONE

from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    tracks: list = field(default_factory=list)

    def add_track(self, track: str):
        pass
