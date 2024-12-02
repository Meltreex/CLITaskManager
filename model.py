from typing import Optional
from datetime import datetime

class Task: 
    def __init__(self, id: int, title: str, data: str,
                description: Optional[str] = None, category: Optional[str] = None, 
                priority: Optional[str] = None, status: bool = False):
        """Конструктор инициализации."""
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.data = self.parse_date(data)
        self.priority = priority
        self.status = status

    def parse_date(self, date_str: str) -> datetime:
        """Преобразуем строковое значение в объект datetime"""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неправильный формат даты. Ожидается YYYY-MM-DD.")
        
    def complete_task(self):
        self.status = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "data": self.data.strftime("%Y-%m-%d"),
            "priority": self.priority,
            "status": self.status,
        }
    
    def __repr__(self):
        self.stat_true = "Выполнена"
        self.stat_false = "Не выполнена"
        self.decoding = "**Отсутствует**"

        return f""" 
        Задача № {self.id}
        Заголовок: {self.title}
        Описание: {self.description if self.description else self.decoding}
        Срок выполнения: {self.data}
        Категория: {self.category if self.category else self.decoding}
        Статус: {self.stat_true if self.status else self.stat_false}
        """