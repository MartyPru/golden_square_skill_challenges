# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

``` python
# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.
```

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicTracker():

    def __init__(self):
        pass

    def add_track(self, track):
        # Parameters:
        #   track: string - name of track
        # Side effects:
        #   Stores track name within list in self object
        #   Raises error message if track already exists in list
        pass

    def list_tracks(self):
        # Returns:
        #   String of tracks the user has added/listened to in easily readable format: e.g. "Tracks you've heard: track 1, track 2"


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
After being given several tracks
returns string with tracks added in easily readable format
"""
# tracker = MusicTracker()
# tracker.add('track 1')
# tracker.add('track 2')
# tracker.list_tracks() => 'Tracks you've heard: track 1, track 2'

"""
If given track that has already been added to list
raises error message letting user know track already exists in list
"""
# tracker = MusicTracker()
# tracker.add('track 1')
# tracker.add('track 1') # raises error 'Track listened to previously!'

"""
If asked to list tracks, but list is empty
raises error message letting user know list is empty
"""
# tracker = MusicTracker()
# tracker.list_tracks() # raises error 'You haven't listened to any tracks!'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._