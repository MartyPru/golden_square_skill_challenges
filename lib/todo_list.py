class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, todo):
        self._tasks.append(todo)
      
    def incomplete(self):
        titles = [todo.task for todo in self._tasks if todo.complete == False]
        return titles

    def complete(self):
        titles = [todo.task for todo in self._tasks if todo.complete == True]
        return titles

    def give_up(self):
        for todo in self._tasks:
            todo.mark_complete()

