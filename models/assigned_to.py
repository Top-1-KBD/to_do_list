"""Module for managing users tasks to be completed."""

from models.task import Task
from models.user import User


class AssignedTo:
    """Represent an association between a task and a user.

    Attributes:
        id: A unique identifier for the task.
        Task: The task.
        User: The users.
    """

    def __init__(self, task: Task, user: User):
        """Initialize a new user instance.

        Args:
            name (str): The name of the users.
            password (str): The password of the users.
            Defaults to an empty string.
        """
        self.id = id(self)  # Unique ID
        self.task = task
        self.user = user

    def get_task(self):
        """Get the task.

        Returns:
            task: the task
        """
        return self.task

    def get_user(self):
        """Get the user.

        Returns:
            user: the user
        """
        return self.user

    def set_task(self, task):
        """Set a task.

        Args:
            task (Task): a specific task
        """
        self.task = task

    def set_user(self, user):
        """Set a user.

        Args:
            user (User): a specific user
        """
        self.user = user
