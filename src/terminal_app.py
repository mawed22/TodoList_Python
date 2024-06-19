import os
import sys
from src.application import Application
from src.task import Task
from src.storage import Storage 

# Classe concrète représentant l'application terminal
class TerminalApp(Application):
    def __init__(self):
        self.tasks = Storage()  # Instance de la classe Storage pour gérer les tâches
        self.running = True

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenue dans le gestionnaire de tâches (Terminal)!")
        while self.running:
            self.display_menu()
            try:
                choice = int(input("Choisissez une option: "))
                self.handle_choice(choice)
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def stop(self):
        print("Arrêt de l'application.")
        self.running = False

    def save_tasks(self, file_path: str):
        self.tasks.save_to_file(file_path)

    def load_tasks(self, file_path: str):
        self.tasks.load_from_file(file_path)

    def display_menu(self):
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Voir les tâches")
        print("3. Modifier une tâche")
        print("4. Supprimer une tâche")
        print("5. Sauvegarder les tâches")
        print("6. Charger les tâches")
        print("7. Quitter")

    def handle_choice(self, choice):   # Gestion des choix de l'utilisateur avec match case
        match choice:
            case 1:
                self.add_task()
            case 2:
                self.view_tasks()
            case 3:
                self.modify_task()
            case 4:
                self.delete_task()
            case 5:
                self.save_tasks('tasks.txt')
            case 6:
                self.load_tasks('tasks.txt')
            case 7:
                self.stop()
            case _:
                print("Choix invalide, veuillez réessayer.")

    def add_task(self):
        title = input("Titre de la tâche: ")
        description = input("Description de la tâche: ")
        task = Task(title, description)
        self.tasks.add_task(task)
        print("Tâche ajoutée.")

    def view_tasks(self):
        for index, task in enumerate(self.tasks.get_tasks()):
            print(f"{index + 1}. {task}")

    def modify_task(self):
        try:
            self.view_tasks()
            task_index = int(input("Entrez le numéro de la tâche à modifier: ")) - 1
            task = self.tasks.get_task(task_index)
            new_title = input(f"Nouvel titre (actuel: {task.title}): ") or task.title
            new_description = input(f"Nouvelle description (actuelle: {task.description}): ") or task.description
            task.set_title(new_title)
            task.set_description(new_description)
            print("Tâche modifiée.")
        except (ValueError, IndexError):
            print("Numéro de tâche invalide.")

    def delete_task(self):
        try:
            self.view_tasks()
            task_index = int(input("Entrez le numéro de la tâche à supprimer: ")) - 1
            self.tasks.delete_task(task_index)
            print("Tâche supprimée.")
        except (ValueError, IndexError):
            print("Numéro de tâche invalide.")
