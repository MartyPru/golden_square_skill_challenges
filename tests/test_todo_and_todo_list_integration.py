from lib.todo import *
from lib.todo_list import *

"""
After being given several tasks
can return a list of incomplete tasks
"""
def test_returns_incomplete_tasks():
    task_1 = Todo('Task 1')
    task_2 = Todo('Task 2')
    task_list = TodoList()
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.incomplete() == ['Task 1', 'Task 2']

"""
After marking tasks as complete
can return a list of complete tasks
"""
def test_returns_complete_list_correctly():
    task_1 = Todo('Task 1')
    task_2 = Todo('Task 2')
    task_list = TodoList()
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.complete() == ['Task 1']


"""
Marks all tasks as complete when giving up
"""
def test_completes_all_when_giving_up():
    task_1 = Todo('Task 1')
    task_2 = Todo('Task 2')
    task_list = TodoList()
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.give_up()
    assert task_list.complete() == ['Task 1', 'Task 2']