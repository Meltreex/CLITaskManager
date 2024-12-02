from Query import TaskManager
from model import Task

def print_menu() -> str:
    print("\nМенеджер задач")
    print("1. Просмотр всех задач")
    print("2. Просмотр задач по категории")
    print("3. Добавить задачу")
    print("4. Изменить задачу")
    print("5. Пометить задачу как выполненную")
    print("6. Удалить задачу")
    print("7. Поиск задач")
    print("8. Выход")

def main(): 
    task_manager = TaskManager("tasks.json")

    while True: 
        print_menu()
        try:
            choice = int(input("Выберите опцию: "))

            if choice == 1:
                task_manager.view_tasks()
            elif choice == 2:
                category = input('Введите категорию: ').capitalize().strip()
                task_manager.view_tasks_category(category)
            elif choice == 3: 
                title = input("Название задачи: ")
                while not title:
                    print("Название задачи является обязательным полем.")  
                    title = input("Название задачи: ")
                description = input("Описание задачи: ")
                category = input("Категория задачи: ")
                data = input("Срок выполнения (YYYY-MM-DD): ")
                priority = input("Приоритет (низкий, средний, высокий): ")

                try: 
                    task = Task(
                        id=task_manager.last_id + 1, 
                        title=title.capitalize().strip(), 
                        description=description.capitalize().strip(),
                        category=category.capitalize().strip(),
                        data=data,
                        priority=priority.capitalize().strip()
                    )
                    task_manager.add_task(task)
                    print("Задача добавлена!")
                except Exception as e:
                    print(f"[INFOR]Error: {e}")
            elif choice == 4:
                id = int(input("Введите номер задачи, которую хотите изменить: "))
                title = input("Новое название: ")
                description = input("Новое описание: ")
                category = input("Новая категория: ")
                data = input("Новый срок выполнения: ")
                priority = input("Новый приоритет: ")

                try: 
                    task = Task(
                        id=id,
                        title=title.capitalize().strip(), 
                        description=description.capitalize().strip(),
                        category=category.capitalize().strip(),
                        data=data,
                        priority=priority.capitalize().strip()
                    )
                    task_manager.update_task(id, task)
                    print("Задача обновлена!")
                except Exception as e:
                    print(f"[INFOR]Error: {e}")
            elif choice == 5:
                id = int(input("Введите номер задачи, которую хотите пометить как выполненную: "))
                task_manager.completed_task(id)
            elif choice == 6:
                id = input("Введите номер задачи для удаления: ")
                category = input("Введите категорию задачи для удаления: ")
                task_manager.delete_task(int(id), category.capitalize().strip(2))
            elif choice == 7:
                keyword = input("Введите ключевое слово для поиска: ")
                category = input("Введите категорию для поиска (оставьте пустым для без фильтра): ")
                status = input("Введите статус (Введите 1 - если выполнена/ 0 - если не выполнена): ")
                tasks = task_manager.search_tasks(keyword, category, status)
                if tasks:
                    for task in tasks:
                        print(task)
                else:
                    print("По вашему запросу ничего не удалось найти!")
            elif choice == 8:
                break
            else: 
                print("Произошла ошибка")
        except Exception as e:
            print(f"[INFOR]Error: {e}\nПожалуйста, следуйте всем подсказкам по работе с интерфейсом!")

if __name__ == "__main__":
    main()