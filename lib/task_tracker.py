class TaskTracker():
    # user-facing properties: n/a
    def __init__(self):
        self._task_list = []
    
    def add_task(self, task):
        self._task_list.append(task)

    def complete_task(self, task):
        if task in self._task_list:
            self._task_list.remove(task)
        else:
            raise Exception("No such task!")

    def list_tasks(self):
        # Returns:
        #   List of tasks stored in object in easily readable format e.g. 'To-do: walk the dog, buy groceries'
        # Side effects:
        #   If no tasks in object, raises an exception
        if len(self._task_list) > 0:
            return f"To-do: {', '.join(self._task_list)}"
        else:
            raise Exception("No tasks set!")