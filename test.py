import tkinter as tk
#from pfc import initialize_game, main


root_Principal = tk.Tk()
root_Principal.title ("Jeu pierre papier et ciseaux !")
root_Principal.geometry ("100x50+500+200")
root_Principal.lift()

tk.Button(root_Principal, text = "Quitter", command = root_Principal.destroy).pack(fill ="both")

root_Controles = tk.Toplevel()
root_Controles.title ("Controles")
root_Controles.geometry("100x50+500+200")

root_Principal.mainloop()
