# Classe représentant une tâche
class Task:
    def __init__(self, title: str, description: str):
        self.title = title  # Titre de la tâche
        self.description = description  # Description de la tâche

    def __str__(self):
        # Représentation textuelle de la tâche
        return f"Tâche: {self.title}, Description: {self.description}"

    def get_title(self):
        # Obtenir le titre de la tâche
        return self.title

    def set_title(self, title: str):
        # Définir le titre de la tâche
        self.title = title

    def get_description(self):
        # Obtenir la description de la tâche
        return self.description

    def set_description(self, description: str):
        # Définir la description de la tâche
        self.description = description
