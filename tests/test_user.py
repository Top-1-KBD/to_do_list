"""Module for testing the User model in the todolist application."""

from models.user import User


def test_task_creation():
    """Test the creation of a task."""
    user = User(name="Test User", password="12345678")
    assert user.name == "Test User"
    assert user.password == "12345678"
