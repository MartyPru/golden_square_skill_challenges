# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

```python
# As a user
# So that I can record my experiences --------
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences ----------
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed ----------

# As a user
# So that I can keep track of my tasks -----------
# I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries ------------
```

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
  ┌────────────────────────────┐
  │                            │
  │ Diary                      │
  │   -init                    │
  │    - self.entries     ┌────┼─────────────┬─────────────────────────┐
  │    - self.todo_list   │    │             │                         │
  │   -add(entry)              │             │                         │
  │   -read                    │             │                         │
  │   -read_in_time(wpm, mins) │             │                         │
  │   -find_numbers            │   ┌─────────▼─────────┐    ┌──────────▼──────────┐
  └────────────────────────────┘   │  DiaryEntry       │    │                     │
                                   │  -init            │    │  TodoList           │
                                   │    -self.title    │    │   -init             │
                                   │    -self.contents │    │     - self.tasks  ──┼────────────────┐
                                   │  -count_words     │    │   -add              │                │
                                   │  -reading_time    │    │   -incomplete       │    ┌───────────▼─────────┐
                                   │  -format          │    │   -complete         │    │                     │
                                   └───────────────────┘    │   -give_up          │    │  ToDo               │
                                                            │                     │    │   -init             │
                                                            └─────────────────────┘    │     -self.task      │
                                                                                       │     -self.complete  │
                                                                                       │   -mark_complete    │
                                                                                       │                     │
                                                                                       │                     │
                                                                                       └─────────────────────┘

```

_Also design the interface of each class in more detail._

```python

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._