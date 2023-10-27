"""Module for testing the AssignedTo model in the todolist application."""

from datetime import datetime, timedelta

from models.assigned_to import AssignedTo
from models.task import Task
from models.user import User


def test_task_creation():
    """Test the creation of a task."""
    task = Task(name="Test Task", description="A simple task",
                start_at=datetime.now(), end_at=datetime.now()+timedelta(days=1))
    user = User(name="Test User", password="12345678")
    assigned_to = AssignedTo(task, user)
    assert assigned_to.task == task
    assert assigned_to.user == user
