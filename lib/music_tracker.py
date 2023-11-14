class MusicTracker():

    def __init__(self):
        self._tracks = []

    def add_track(self, track):
        if track in self._tracks:
            raise Exception('Track listened to previously!')
        self._tracks.append(track)

    def list_tracks(self):
       if len(self._tracks) == 0:
           raise Exception("You haven't listened to any tracks!")
       return f"Tracks you've heard: {', '.join(self._tracks)}"