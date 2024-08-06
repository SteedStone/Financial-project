import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Importer le module ttk pour les widgets améliorés
import pandas as pd
from Appli_copy import *

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface utilisateur")

        # Création des widgets pour les paramètres
        self.param_frame = ttk.Frame(self.master, padding=10)
        self.param_frame.pack()

        # Utilisation de ttk.Label pour un meilleur style
        ttk.Label(self.param_frame, text="Nombre de périodes:").grid(row=0, column=0, sticky="w")
        self.nb_periodes_entry = ttk.Entry(self.param_frame)
        self.nb_periodes_entry.grid(row=0, column=1)

        ttk.Label(self.param_frame, text="Montant de l'emprunt:").grid(row=1, column=0, sticky="w")
        self.montant_emprunt_entry = ttk.Entry(self.param_frame)
        self.montant_emprunt_entry.grid(row=1, column=1)

        ttk.Label(self.param_frame, text="Taux d'intérêt annuel:").grid(row=2, column=0, sticky="w")
        self.taux_interet_annuel_entry = ttk.Entry(self.param_frame)
        self.taux_interet_annuel_entry.grid(row=2, column=1)

        ttk.Label(self.param_frame, text="Prépayment:").grid(row=3, column=0, sticky="w")
        self.prepayment_entry = ttk.Entry(self.param_frame)
        self.prepayment_entry.grid(row=3, column=1)

        ttk.Label(self.param_frame, text="Nombre de paiements par an:").grid(row=4, column=0, sticky="w")
        self.nombre_de_payment_par_an_entry = ttk.Entry(self.param_frame)
        self.nombre_de_payment_par_an_entry.grid(row=4, column=1)

        ttk.Label(self.param_frame, text="Durée de remplacement (années):").grid(row=5, column=0, sticky="w")
        self.Duree_repracing_anne_entry = ttk.Entry(self.param_frame)
        self.Duree_repracing_anne_entry.grid(row=5, column=1)

        ttk.Label(self.param_frame, text="Période:").grid(row=6, column=0, sticky="w")
        self.per_entry = ttk.Entry(self.param_frame)
        self.per_entry.grid(row=6, column=1)

        # Bouton pour charger le fichier Excel
        self.load_button = ttk.Button(self.param_frame, text="Charger le fichier Excel", command=self.load_excel)
        self.load_button.grid(row=7, column=0, columnspan=2)

        # Création des widgets pour afficher les données
        self.data_frame = ttk.Frame(self.master, padding=10)
        self.data_frame.pack()

        self.nb_periodes = tk.StringVar()
        self.montant_emprunt = tk.StringVar()

    def load_excel(self):
        # Charger le fichier Excel
        # Traitez les données et mettez à jour les widgets d'affichage
        nb_periodes = int(self.nb_periodes_entry.get())
        montant_emprunt = int(self.montant_emprunt_entry.get())
        taux_interet_annuel = float(self.taux_interet_annuel_entry.get())
        prepayment = float(self.prepayment_entry.get())  # Convertir en float si nécessaire
        nombre_de_payment_par_an = int(self.nombre_de_payment_par_an_entry.get())
        Duree_repracing_anne = int(self.Duree_repracing_anne_entry.get())
        per = int(self.per_entry.get())
        param = Parametres(nb_periodes, montant_emprunt, taux_interet_annuel, prepayment, nombre_de_payment_par_an, Duree_repracing_anne, per)
        chemin_fichier = r"C:\Users\guera\OneDrive - UCL\Bureau\Papa\Calcul Hedging_Rates_BBG_based_NEW_INCL_SECUR_Factor_V2.2_frozen.xlsm"

        # Création des instances
        gestion_fichier = GestionFichier(chemin_fichier)
        calculs = Calculs(param, gestion_fichier)
        print("Résultat du calcul :", calculs.retourne_valeurs_attendue())

def main():
    root = tk.Tk()
    app = GUI(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
