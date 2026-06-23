from dataclasses2 import Playlist


def test_add_track():
    p = Playlist("Chill")
    p.add_track("Song A")
    p.add_track("Song B")
    assert p.tracks == ["Song A", "Song B"]

def test_separate_instances():
    p1 = Playlist("Chill")
    p2 = Playlist("Workout")
    p1.add_track("Song A")
    assert p2.tracks == []

def test_empty_initially():
    p = Playlist("Empty")
    assert p.tracks == []
