from datetime import datetime

try :
    def ecrire_fichier(msg):
        f = open("phonerBook.log", "a")
        date = str(datetime.now())
        f.write(date + " ")
        f.write(msg + "\n")
        f.close()
except IndexError as e:
    print(f"mon erreur = {e}")





