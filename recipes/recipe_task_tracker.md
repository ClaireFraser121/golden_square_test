# Task Tracker Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep tra taskck of
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TaskTracker():
    def add(self, task):
        #Pasrameters:
        #   task: string, representing a task
        pass

    def list_incomplete(self):
        # Returns:
        #   A list of incomplete tasks
        pass

    def mark_complete(self, index):
        # Parameters:
        #   index: an intereger representing the task to complete
        # Side-effect:
        #   Removes the task at index from the list of tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
Initially, there are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete() # => []


"""
When we add a task 
It is reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.list_incomplete() # => ["Walk the dog"]

"""
When we add multiple task 
They are reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the cat")
tracker.add("Walk the frog")
tracker.list_incomplete() 
    # => ["Walk the dog", "Walk the cat", "Walk the frog"]

"""
When we add multiple task 
And mark one as complete
it disappears from the task list
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the cat")
tracker.add("Walk the frog")
tracker.list_incomplete() 
    # => ["Walk the dog", "Walk the frog"]

"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.mark_complete(-1) # Raises an error "No such task to mark complete"

"""
If we try to mark a track complete that does not exist (too high)
It raises an error
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.mark_complete(2) # Raise an error "No such task to mark complete"
tracker.list_incomplete() # => ["Walk the dog"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
