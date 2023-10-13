import pytest
from todolist.models.task_list import TaskList

def test_add_task():
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    assert len(task_list.tasks) == 1

def test_remove_task():
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.remove_task("Buy Groceries")
    assert len(task_list.tasks) == 0

def test_complete_task():
    task_list = TaskList()
    task_list.add_task("Buy Groceries", "Buy fruits and vegetables")
    task_list.complete_task("Buy Groceries")
    assert task_list.tasks[0].completed == True
