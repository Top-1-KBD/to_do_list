"""Module for testing the TaskList model in the todolist application."""

from datetime import datetime
import pytest
from models.task_list import TaskList
from exceptions.task_exceptions import TaskNotFoundError


def test_add_task():
    """Test the creation of a list of task and addition of a task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    assert len(task_list.tasks) == 1


def test_remove_task():
    """Test the action of removing of a task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.remove_task("Buy Groceries")
    assert len(task_list.tasks) == 0


def test_remove_task_failure():
    """Test the exception raised when removing a task that does not exist."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    with pytest.raises(TaskNotFoundError, match="Task not found!"):
        task_list.remove_task("Go for a run")


def test_to_do_task():
    """Test the action of a task to do."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.to_do_task("Buy Groceries",
                         start_at=datetime.strptime("2023-01-01", "%Y-%m-%d"),
                         end_at=datetime.strptime("2023-01-02", "%Y-%m-%d"))
    assert task_list.tasks[0].status == "to do"
    assert task_list.tasks[0].start_at == datetime.strptime(
        "2023-01-01", "%Y-%m-%d")
    assert task_list.tasks[0].end_at == datetime.strptime(
        "2023-01-02", "%Y-%m-%d")


def test_doing_task():
    """Test the action of doing a task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.doing_task("Buy Groceries")
    assert task_list.tasks[0].status == "doing"


def test_succeeded_task():
    """Test the action of succeeding a task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.succeeded_task("Buy Groceries")
    assert task_list.tasks[0].status == "succeeded"


def test_failed_task():
    """Test the action of a failed task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.failed_task("Buy Groceries")
    assert task_list.tasks[0].status == "failed"


def test_display_tasks():
    """Test the display of uncompleted tasks."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.add_task("Go for a run", "5km run in the morning")
    task_list.succeeded_task("Buy Groceries")

    displayed_tasks = task_list.display_tasks()
    assert len(displayed_tasks) == 1
    assert displayed_tasks[0] == "Go for a run - 5km run in the morning"
