import json
from model import Task
from typing import Optional

class TaskManager:
    def __init__(self, storage_file: str):
        #Конструктор инициализации
        self.storage_file = storage_file
        self.tasks = self.load_tasks()
        self.last_id = max([task.id for task in self.tasks], default=0)
        
    def load_tasks(self):
        #Загружаем задачи из файла JSON.
        try: 
            with open(self.storage_file, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []
        
    def save_tasks(self):
        #Сохраняем текущие задачи в файл JSON.
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks], 
                file, 
                ensure_ascii=False,
                indent=4
            )

    def add_task(self, task: Task):
        #Добавляет новую задачу
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        #Выводит все задачи
        tasks_display = [task for task in self.tasks]
        for task in tasks_display:
            print(task)

    def view_tasks_category(self, category: Optional[str] = None):
        #Выводит задачи по заданной категории
        tasks_display = [task for task in self.tasks if task.category == category]
        for task in tasks_display:
            print(task)

    def update_task(self, id: int, task: Task):
        #Обновляет задачу по заданному ID.
        for tsk in self.tasks:
            if tsk.id == id:
                tsk.title = task.title
                tsk.description = task.description
                tsk.category = task.category
                tsk.data = task.data
                tsk.priority = task.priority
                self.save_tasks()
                break
            else:
                print(f"Задачи под номером {id} не существует!")
                break
                

    def completed_task(self, id: int):
        #Помечает задачу как выполненную
        for task in self.tasks:
            if task.id == id:
                task.complete_task() # Меняем статус
                self.save_tasks()
                break
            else:
                print(f"Задачи под номером {id} не существует!")
                break

    def delete_task(self, id: Optional[int] = None, category: Optional[str] = None):
        if id:
            self.tasks = [task for task in self.tasks if task.id != id]
        elif category:
            self.tasks = [task for task in self.tasks if task.category != category]
        else:
            print(f"Задачи c номером {id} или категорий {category} не существует!")
        self.save_tasks()

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None, status: Optional[str] = None):
        
        if status:
            if status == "1":
                status = True
            elif status == "0":
                status = False
            else:
                raise ValueError("Неверное значение статуса.")

        return [task for task in self.tasks if
                (keyword.lower().strip() in task.title.lower() or keyword.lower().strip() in task.description.lower() if keyword else True) and
                (task.category.lower() == category.lower().strip() if category else True) and
                (task.status == status if status is not None else True)]

