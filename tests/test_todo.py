from lib.todo import *

"""
When initiated with task
can return what the task is as a string
"""
def test_returns_task_when_asked():
    task_1 = Todo('Test-drive a class system')
    assert task_1.task == "Test-drive a class system"


"""
When first initiated,
task is not complete
"""

def test_task_not_complete_on_start():
    task_1 = Todo('Test-drive a class system')
    assert task_1.complete == False


"""
When asked to complete task
sets complete status to True
"""

def test_task_complete_when_asked():
    task_1 = Todo('Test-drive a class system')
    task_1.mark_complete()
    assert task_1.complete == True