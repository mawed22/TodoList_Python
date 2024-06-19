from abc import ABC, abstractmethod

# Classe abstraite représentant l'application
class Application(ABC):
    @abstractmethod
    def run(self):
        pass 

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def save_tasks(self, file_path: str):
        pass

    @abstractmethod
    def load_tasks(self, file_path: str):
        pass
