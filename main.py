# fichier principal : main.py
import tkinter as tk
from mes_fonctions import dire_bonjour, ajouter

# Création de l'interface Tkinter
def creer_interface():
    def on_click_bonjour():
        dire_bonjour()

    def on_click_add():
        resultat = ajouter(10, 20)
        label_resultat.config(text=f"Résultat : {resultat}")

    root = tk.Tk()
    root.title("Interface Girly")

    # Bouton 1 - Appeler dire_bonjour
    btn_bonjour = tk.Button(root, text="Dire Bonjour", command=on_click_bonjour)
    btn_bonjour.pack(pady=10)

    # Bouton 2 - Ajouter deux nombres
    btn_add = tk.Button(root, text="Ajouter 10 + 20", command=on_click_add)
    btn_add.pack(pady=10)

    # Label pour afficher le résultat
    global label_resultat
    label_resultat = tk.Label(root, text="Résultat :")
    label_resultat.pack(pady=10)

    root.mainloop()

# Lance l'interface
if __name__ == "__main__":
    creer_interface()