
# Gestionnaire de Tâches

Ce projet est un gestionnaire de tâches simple permettant aux utilisateurs de créer, afficher, modifier, et supprimer des tâches. Il propose deux interfaces : une interface en ligne de commande (terminal) et une interface graphique (GUI) utilisant `tkinter`.

## Fonctionnalités

### Interface Terminal

- Ajouter une tâche : Permet à l'utilisateur de créer une nouvelle tâche en entrant un titre et une description.
- **Voir les tâches** : Affiche la liste des tâches avec leurs titres et descriptions.
- **Modifier une tâche** : Permet à l'utilisateur de modifier le titre et/ou la description d'une tâche existante.
- **Supprimer une tâche** : Permet à l'utilisateur de supprimer une tâche de la liste.
- **Sauvegarder les tâches** : Sauvegarde les tâches dans un fichier texte.
- **Charger les tâches** : Charge les tâches à partir d'un fichier texte.
- **Quitter l'application** : Quitte l'application de gestion des tâches.

### Interface Graphique (GUI)

- **Ajouter une tâche** : Interface utilisateur pour créer une nouvelle tâche avec des champs de saisie pour le titre et la description.
- **Voir les tâches** : Affiche les tâches dans une boîte de dialogue.
- **Modifier une tâche** : Interface utilisateur pour sélectionner et modifier le titre et/ou la description d'une tâche existante.
- **Supprimer une tâche** : Interface utilisateur pour sélectionner et supprimer une tâche de la liste.
- **Sauvegarder les tâches** : Sauvegarde les tâches dans un fichier texte spécifié par l'utilisateur.
- **Charger les tâches** : Charge les tâches à partir d'un fichier texte spécifié par l'utilisateur.

## Installation et Exécution

### Prérequis

- Python 3.x
- Bibliothèque `tkinter`

### Installation

1. Clonez ce dépôt sur votre machine locale :

   ```sh
   git clone https://github.com/mawed22/TodoList_Python
   cd gestionnaire-de-taches
   ```

2. Installez la bibliothèque `tkinter` :

   ```sh
   pip install customtkinter
   ```

### Exécution

1. Pour exécuter l'application, utilisez la commande suivante :

   ```sh
   python main.py
   ```

2. Vous serez invité à choisir entre l'interface terminal ou l'interface graphique :

   - Entrez `1` pour l'interface terminal.
   - Entrez `2` pour l'interface graphique.

### Détails des Fichiers

- **main.py** : Point d'entrée de l'application. Permet de choisir entre l'interface terminal et l'interface graphique.
- **src/application.py** : Contient la classe abstraite `Application` définissant les méthodes de base pour les applications terminal et GUI.
- **src/task.py** : Définit la classe `Task` représentant une tâche avec des méthodes getter et setter pour le titre et la description.
- **src/storage.py** : Gère le stockage des tâches, y compris les méthodes pour ajouter, supprimer, sauvegarder et charger les tâches depuis un fichier texte.
- **src/terminal_app.py** : Implémente l'application terminal en utilisant la classe `Application`.
- **src/gui_app.py** : Implémente l'application GUI en utilisant `tkinter` et la classe `Application`.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une issue ou une pull request pour toute suggestion ou amélioration.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

# Auteur: Foupoua Mohamed