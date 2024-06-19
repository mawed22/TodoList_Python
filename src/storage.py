import os
from src.task import Task

# Classe représentant le stockage des tâches
class Storage:
    def __init__(self):
        self.tasks = []  # Liste des tâches

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def get_task(self, index: int):
        return self.tasks[index]

    def delete_task(self, index: int):
        del self.tasks[index]

    def save_to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description}\n")

    def load_from_file(self, file_path: str):  # Charger les tâches depuis un fichier
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.tasks = []
                for line in file:
                    title, description = line.strip().split(',')
                    self.tasks.append(Task(title, description))
