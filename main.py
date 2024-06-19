from src.terminal_app import TerminalApp
from src.gui_app import GUIApp

def main():
    print("\n Bienvenue sur le votre gestionnaire de tache.")
    name_user = input("Entrer votre nom : ")
    print(f"\n Salut {name_user}, choisi l'interface : ")
    choice = input("\n (1: Terminal, 2: GUI(Interface Graphique)): ")
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
