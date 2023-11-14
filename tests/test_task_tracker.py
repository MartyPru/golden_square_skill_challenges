from lib.task_tracker import *
import pytest

"""
Given several tasks
can return a list of tasks in easily readable format
"""
def test_list_tasks_correctly():
    task_tracker = TaskTracker()
    task_tracker.add_task('walk the dog')
    task_tracker.add_task('buy groceries')
    result = task_tracker.list_tasks()
    assert result == 'To-do: walk the dog, buy groceries'


"""
If task marked as complete
removes task from list
"""
def test_removes_completed_task():
    task_tracker = TaskTracker()
    task_tracker.add_task('walk the dog')
    task_tracker.add_task('buy groceries')
    task_tracker.complete_task('walk the dog')
    result = task_tracker.list_tasks()
    assert result == 'To-do: buy groceries'

"""
If asked to complete task that doesn't exist
raises error
"""
def test_raises_error_if_completing_false_task():
    task_tracker = TaskTracker()
    task_tracker.add_task('buy groceries')
    with pytest.raises(Exception) as e:
        task_tracker.complete_task('walk the dog')
    error_message = str(e.value)
    assert error_message == 'No such task!'

"""
If asked to list tasks but no tasks exist
raises exception
"""
def test_raises_error_if_no_tasks_when_listing():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.list_tasks()
    error_message = str(e.value)
    assert error_message == 'No tasks set!'