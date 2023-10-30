"""Module for testing the Task model in the todolist application."""

from datetime import datetime
from models.task import Task


def test_task_creation():
    """Test the creation of a task."""
    task = Task(name="Test Task", description="A simple task",
                start_at=datetime.strptime("2023-01-01", "%Y-%m-%d"), end_at=datetime.strptime("2023-01-02", "%Y-%m-%d"))
    assert task.name == "Test Task"
    assert task.description == "A simple task"
    assert task.start_at == datetime.strptime("2023-01-01", "%Y-%m-%d")
    assert task.end_at == datetime.strptime("2023-01-02", "%Y-%m-%d")


def test_mark_as_to_do():
    """Test marking a task as to do."""
    task = Task(name="Test Task", description="A simple task",
                start_at=datetime.strptime("2023-01-01", "%Y-%m-%d"), end_at=datetime.strptime("2023-01-01", "%Y-%m-%d"))
    task.mark_as_to_do(start_at=datetime.strptime("2023-01-04", "%Y-%m-%d"),
                       end_at=datetime.strptime("2023-01-05", "%Y-%m-%d"))
    assert task.status == "to do"
    assert task.start_at == datetime.strptime("2023-01-04", "%Y-%m-%d")
    assert task.end_at == datetime.strptime("2023-01-05", "%Y-%m-%d")


def test_mark_as_doing():
    """Test marking a task as doing."""
    task = Task(name="Test Task", description="A simple task", start_at=datetime.strptime(
        "2023-10-27", "%Y-%m-%d"), end_at=datetime.strptime("2023-10-27", "%Y-%m-%d"))
    task.mark_as_doing()
    assert task.status == "doing"


def test_mark_as_failed():
    """Test marking a task as failed."""
    task = Task(name="Test Task", description="A simple task", start_at=datetime.strptime(
        "2023-10-27", "%Y-%m-%d"), end_at=datetime.strptime("2023-10-27", "%Y-%m-%d"))
    task.mark_as_failed()
    assert task.status == "failed"


def test_mark_as_succeeded():
    """Test marking a task as succeeded."""
    task = Task(name="Test Task", description="A simple task", start_at=datetime.strptime(
        "2023-10-27", "%Y-%m-%d"), end_at=datetime.strptime("2023-10-27", "%Y-%m-%d"))
    task.mark_as_succeeded()
    assert task.status == "succeeded"
