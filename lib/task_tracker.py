class TaskTracker():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def list_incomplete(self):
        return self._tasks

    def mark_complete(self, index):
        if index < 0 or index >= len(self._tasks):
            raise Exception("No such task to mark complete")
        del self._tasks[index]