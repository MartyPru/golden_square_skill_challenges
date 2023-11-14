import pytest
from lib.music_tracker import *

"""
After being given several tracks
returns string with tracks added in easily readable format
"""
def test_adds_tracks_and_lists_correctly():
    tracker = MusicTracker()
    tracker.add_track('track 1')
    tracker.add_track('track 2')
    result = tracker.list_tracks()
    assert result == "Tracks you've heard: track 1, track 2"

def test_adds_different_tracks_and_lists_correctly():
    tracker = MusicTracker()
    tracker.add_track('track 3')
    tracker.add_track('track 4')
    result = tracker.list_tracks()
    assert result == "Tracks you've heard: track 3, track 4"

"""
If given track that has already been added to list
raises error message letting user know track already exists in list
"""
def test_raises_error_if_duplicate_track():
    tracker = MusicTracker()
    tracker.add_track('track 1')
    with pytest.raises(Exception) as e:
        tracker.add_track('track 1')
    error_message = str(e.value)
    assert error_message == 'Track listened to previously!'

"""
If asked to list tracks, but list is empty
raises error message letting user know list is empty
"""
def test_raises_error_if_listing_when_no_tracks_in_list():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.list_tracks()
    error_message = str(e.value)
    assert error_message == "You haven't listened to any tracks!"