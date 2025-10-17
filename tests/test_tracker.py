from lib.task_tracker import TaskTracker
import pytest

"""
Initially, there are no tasks
"""
def test_initial_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []


"""
When we add a task 
It is reflected in the list of tasks
"""
def test_add_task_reflected_in_task_list():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
When we add multiple task 
They are reflected in the list of tasks
"""
def test_add_multiple_tasks_reflected_in_task_list():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    assert tracker.list_incomplete() == [
        "Walk the dog", "Walk the cat", "Walk the frog"]
        
"""
When we add multiple task 
And mark one as complete
it disappears from the task list
"""
def test_mark_task_complete_removes_from_task_list():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == [
        "Walk the dog", "Walk the frog"]

"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
def test_mark_task_that_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1) 
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
If we try to mark a track complete that does not exist (too high)
It raises an error
"""
def test_mark_task_that_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(2) 
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]