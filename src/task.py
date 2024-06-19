# Classe représentant une tâche
class Task:
    def __init__(self, title: str, description: str):
        self.title = title  # Titre de la tâche
        self.description = description  # Description de la tâche

    def __str__(self):
        return f"Tâche: {self.title}, Description: {self.description}"

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description: str):
        self.description = description
