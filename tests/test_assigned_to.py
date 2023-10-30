"""Module for testing the AssignedTo model in the todolist application."""

from datetime import datetime

from models.assigned_to import AssignedTo
from models.task import Task
from models.user import User


def test_task_creation():
    """Test the creation of a task."""
    task = Task(name="Test Task", description="A simple task",
                start_at=datetime.strptime("2023-10-27", "%Y-%m-%d"),
                end_at=datetime.strptime("2023-10-27", "%Y-%m-%d"))
    user = User(name="Test User", password="12345678")
    assigned_to = AssignedTo(task, user)
    assert assigned_to.task == task
    assert assigned_to.user == user
