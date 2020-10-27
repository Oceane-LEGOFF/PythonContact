import logger
programme = True

try :
    def create_contact(names, phone_number, is_favorite):
        contact = {
            "names": names,
            "phone_number": phone_number,
            "is_favorite": is_favorite,
        }
        return contact
except IndexError as e:
    print(f"mon erreur = {e}")

annuaire = {}


def add_contact(new):
    logger.ecrire_fichier("Ajout d'un contact")
    # trier nom par ordre alphabetik
    phone_number = new["phone_number"]
    annuaire[phone_number] = new


def get_names(n):
    names = n["names"]
    # get nom contact
    annuaire[get_names] = n
    return names


def get_number(c):
    phone_number = c["phone_number"]
    annuaire[phone_number] = c
    return phone_number


def get_fav(f):
    favoris = f["favoris"]
    annuaire[get_fav] = f
    return favoris


while programme:
        names = input("Entrez nom du nouveau contact :")
        phone_number = input("Entrez numero du nouveau contact :")
        is_favorite = input("Voulez vous l'ajouter en Favoris ?")

        c = create_contact(names, phone_number, is_favorite)
        add_contact(c)
        print(annuaire)