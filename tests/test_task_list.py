"""Module for testing the TaskList model in the todolist application."""

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


def test_complete_task():
    """Test the action of completing a task."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.complete_task("Buy Groceries")
    assert task_list.tasks[0].completed == 1


def test_display_tasks():
    """Test the display of uncompleted tasks."""
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.add_task("Go for a run", "5km run in the morning")
    task_list.complete_task("Buy Groceries")

    displayed_tasks = task_list.display_tasks()
    assert len(displayed_tasks) == 1
    assert displayed_tasks[0] == "Go for a run - 5km run in the morning"
