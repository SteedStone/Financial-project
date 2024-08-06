import tkinter as tk
from tkinter import ttk
import threading
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application Tkinter avec Threads")

        # Créer un bouton pour démarrer le traitement
        self.start_button = ttk.Button(self, text="Démarrer le traitement", command=self.start_long_task)
        self.start_button.pack(padx=20, pady=20)

        # Créer une étiquette pour afficher le statut
        self.status_label = ttk.Label(self, text="Prêt")
        self.status_label.pack(padx=20, pady=20)

    def start_long_task(self):
        # Mettre à jour l'étiquette pour indiquer que le traitement commence
        self.status_label.config(text="Traitement en cours...")
        
        # Créer et démarrer un thread pour exécuter la tâche longue
        thread = threading.Thread(target=self.long_task)
        thread.start()

    def long_task(self):
        # Simuler une tâche longue
        time.sleep(5)
        
        # Mettre à jour l'interface après la fin de la tâche
        self.after(0, self.on_task_complete)

    def on_task_complete(self):
        # Mettre à jour l'étiquette pour indiquer que le traitement est terminé
        self.status_label.config(text="Traitement terminé")

if __name__ == "__main__":
    app = Application()
    app.mainloop()