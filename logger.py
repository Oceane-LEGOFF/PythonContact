from datetime import datetime

def ecrire_fichier(msg):
    f = open("phonerBook.log", "a")
    date = str(datetime.now())
    f.write(date + " ")
    f.write(msg + "\n")
    f.close()


# try:
# #permet de continuer a faire tourner le programme meme si il y a une erreur
# except IndexError as e:
# print(f"mon erreur = {e}")