import tkinter as tk
from tkinter import messagebox, simpledialog
from src.application import Application
from src.task import Task
from src.storage import Storage

# Classe concrète représentant l'application GUI
class GUIApp(Application):
    def __init__(self):
        self.tasks = Storage()  # Instance de la classe Storage pour gérer les tâches
        self.root = tk.Tk()
        self.root.title("Gestionnaire de Tâches")

    def run(self):
        # Méthode pour démarrer l'application GUI
        self.setup_gui()
        self.root.mainloop()

    def stop(self):
        # Méthode pour arrêter l'application
        self.root.destroy()

    def setup_gui(self):
        # Configuration de l'interface utilisateur
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.title_entry = tk.Entry(self.frame)
        self.title_entry.pack()
        self.title_entry.insert(0, "Titre")

        self.desc_entry = tk.Entry(self.frame)
        self.desc_entry.pack()
        self.desc_entry.insert(0, "Description")

        self.add_button = tk.Button(self.frame, text="Ajouter Tâche", command=self.add_task)
        self.add_button.pack()

        self.view_button = tk.Button(self.frame, text="Voir Tâches", command=self.view_tasks)
        self.view_button.pack()

        self.modify_button = tk.Button(self.frame, text="Modifier Tâche", command=self.modify_task)
        self.modify_button.pack()

        self.delete_button = tk.Button(self.frame, text="Supprimer Tâche", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(self.frame, text="Sauvegarder Tâches", command=lambda: self.save_tasks('tasks.txt'))
        self.save_button.pack()

        self.load_button = tk.Button(self.frame, text="Charger Tâches", command=lambda: self.load_tasks('tasks.txt'))
        self.load_button.pack()

    def add_task(self):
        # Ajout d'une tâche
        title = self.title_entry.get()
        description = self.desc_entry.get()
        task = Task(title, description)
        self.tasks.add_task(task)
        messagebox.showinfo("Info", "Tâche ajoutée.")

    def view_tasks(self):
        # Affichage des tâches
        tasks_str = "\n".join(f"{index + 1}. {task}" for index, task in enumerate(self.tasks.get_tasks()))
        messagebox.showinfo("Tâches", tasks_str)

    def modify_task(self):
        # Modification d'une tâche
        task_index = simpledialog.askinteger("Modifier Tâche", "Entrez le numéro de la tâche à modifier:") - 1
        if task_index is not None and 0 <= task_index < len(self.tasks.get_tasks()):
            task = self.tasks.get_task(task_index)
            new_title = simpledialog.askstring("Modifier Tâche", f"Nouvel titre (actuel: {task.title}):", initialvalue=task.title)
            new_description = simpledialog.askstring("Modifier Tâche", f"Nouvelle description (actuelle: {task.description}):", initialvalue=task.description)
            if new_title:
                task.set_title(new_title)
            if new_description:
                task.set_description(new_description)
            messagebox.showinfo("Info", "Tâche modifiée.")
        else:
            messagebox.showerror("Erreur", "Numéro de tâche invalide.")

    def delete_task(self):
        # Suppression d'une tâche
        task_index = simpledialog.askinteger("Supprimer Tâche", "Entrez le numéro de la tâche à supprimer:") - 1
        if task_index is not None and 0 <= task_index < len(self.tasks.get_tasks()):
            self.tasks.delete_task(task_index)
            messagebox.showinfo("Info", "Tâche supprimée.")
        else:
            messagebox.showerror("Erreur", "Numéro de tâche invalide.")

    def save_tasks(self, file_path: str):
        # Sauvegarde des tâches
        self.tasks.save_to_file(file_path)
        messagebox.showinfo("Info", "Tâches sauvegardées.")

    def load_tasks(self, file_path: str):
        # Chargement des tâches
        self.tasks.load_from_file(file_path)
        messagebox.showinfo("Info", "Tâches chargées.")
