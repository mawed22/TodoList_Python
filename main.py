from src.terminal_app import TerminalApp
from src.gui_app import GUIApp

def main():
    # Demander à l'utilisateur de choisir l'interface
    choice = input("Choisissez l'interface (1: Terminal, 2: GUI(Interface Graphique)): ")
    if choice == '1':
        app = TerminalApp()
    elif choice == '2':
        app = GUIApp()
    else:
        print("Choix invalide.")
        return

    # Démarrer l'application
    app.run()

if __name__ == "__main__":
    main()
