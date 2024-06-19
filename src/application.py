from abc import ABC, abstractmethod

# Classe abstraite représentant l'application
class Application(ABC):
    @abstractmethod
    def run(self):
        # Méthode pour démarrer l'application
        pass 

    @abstractmethod
    def stop(self):
        # Méthode pour arrêter l'application
        pass

    @abstractmethod
    def save_tasks(self, file_path: str):
        # Méthode pour sauvegarder les tâches
        pass

    @abstractmethod
    def load_tasks(self, file_path: str):
        # Méthode pour charger les tâches
        pass
