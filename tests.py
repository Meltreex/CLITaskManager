import pytest
from datetime import datetime
from model import Task
from Query import TaskManager

# Создание теста с очисткой файла JSON перед каждым тестом
@pytest.fixture
def task_manager():
    task_manager = TaskManager('test_tasks.json')
    task_manager.last_id = 0  # Сброс ID перед каждым тестом

    task_manager.tasks = []  # Очистим список задач
    task_manager.save_tasks() 

    return task_manager

# Тест для создания задачи
def test_task_creation(task_manager):
    task = Task(id=task_manager.last_id + 1, title="Test Task", description="This is a test task", category="Test", data="2024-12-01", priority="Medium")
    task_manager.add_task(task)
    
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Test Task"

# Тест для изменения статуса задачи на выполненный
def test_complete_task(task_manager):
    task = Task(id=task_manager.last_id + 1, title="Task to be completed", description="Complete this task", category="Test", data="2024-12-01", priority="Medium")
    task_manager.add_task(task)
    
    task_manager.completed_task(task.id)

    assert task_manager.tasks[0].status is True
    assert task_manager.tasks[0].title == "Task to be completed"

# Тест для поиска задач по ключевому слову
def test_search_task_by_keyword(task_manager):
    task1 = Task(id=task_manager.last_id + 1, title="Test Task 1", description="Description of task 1", category="Test", data="2024-12-01", priority="Low")
    task2 = Task(id=task_manager.last_id + 1, title="Another Task", description="Description of task 2", category="Work", data="2024-12-05", priority="High")
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    
    # Поиск по ключевому слову "Test"
    tasks = task_manager.search_tasks(keyword="Test", category = None, status = None)
    
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task 1"
    
    # Поиск по ключевому слову "Another"
    tasks = task_manager.search_tasks(keyword="Another", category = None, status = None)

    assert len(tasks) == 1
    assert tasks[0].title == "Another Task"

# Тест для поиска задач по категории
def test_search_task_by_category(task_manager):
    task1 = Task(id=task_manager.last_id + 1, title="Work Task", description="Description for work task", category="Work", data="2024-12-01", priority="Low")
    task2 = Task(id=task_manager.last_id + 1, title="Personal Task", description="Description for personal task", category="Personal", data="2024-12-05", priority="High")
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    
    # Поиск по категории "Work"
    tasks = task_manager.search_tasks(keyword = None, category = "Work", status = None)
    
    assert len(tasks) == 1
    assert tasks[0].category == "Work"
    
    # Поиск по категории "Personal"
    tasks = task_manager.search_tasks(keyword = None, category = "Personal", status = None)

    assert len(tasks) == 1
    assert tasks[0].category == "Personal"

# Тест для поиска задач по статусу
def test_search_task_by_status(task_manager):
    task1 = Task(id=task_manager.last_id + 1, title="Task 1", description="Description for task 1", category="Work", data="2024-12-01", priority="Low", status=False)
    task2 = Task(id=task_manager.last_id + 1, title="Task 2", description="Description for task 2", category="Personal", data="2024-12-05", priority="High", status=True)
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    
    # Поиск по статусу "выполнена" (True)
    tasks = task_manager.search_tasks(keyword = None, category = None, status="1")
    
    assert len(tasks) == 1
    assert tasks[0].status is True
    assert tasks[0].title == "Task 2"
    
    # Поиск по статусу "не выполнена" (False)
    tasks = task_manager.search_tasks(keyword = None, category = None, status="0")
    
    assert len(tasks) == 1
    assert tasks[0].status is False
    assert tasks[0].title == "Task 1"

# Тест для удаления задачи
def test_delete_task(task_manager):
    task = Task(id=task_manager.last_id + 1, title="Task to be deleted", description="Delete this task", category="Test", data="2024-12-01", priority="Low")
    task_manager.add_task(task)
    
    task_manager.delete_task(id=task.id)
    
    assert len(task_manager.tasks) == 0
