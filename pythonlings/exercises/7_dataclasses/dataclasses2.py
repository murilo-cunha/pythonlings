# I AM NOT DONE

from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    tracks: list = field(default_factory=list)  # This is correct — study it

    def add_track(self, track: str):
        # Fix: append track to self.tracks
        pass


# DON'T EDIT THE TESTS
p1 = Playlist("Chill")
p2 = Playlist("Workout")

p1.add_track("Song A")
p1.add_track("Song B")

assert p1.tracks == ["Song A", "Song B"]
assert p2.tracks == []  # Separate list per instance (default_factory)
