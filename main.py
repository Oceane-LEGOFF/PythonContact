from art import *
print(text2art("PHONEBOOK", font="block"))
programe = True

def create_contact(names, phone_number, is_favorite):
        contact = {
                "names": names,
                "phone_number": phone_number,
                "is_favorite": is_favorite,
        }
        return contact

annuaire = {}
def add_contact(new):
        #trier nom par ordre alphabetik
        phone_number=new["phone_number"]

        annuaire [phone_number] = new

def get_names(n):
        names = n["names"]
        #reccup nom chaque contact
        annuaire[get_names] = n

        #trier nom par ordre alphabetique
        return names

def get_number(c):
        phone_number = c["phone_number"]
        annuaire[phone_number] = c
        return phone_number

def get_fav(f):
        favoris = f["favoris"]
        annuaire[get_fav] = f

        #trier nom par ordre alphabetik
        return favoris


while programe:
        names = input("Entrez nom du nouveau contact :")
        phone_number = input("Entrez numero du nouveau contact :")
        is_favorite = input("Voulez vous l'ajouter en Favoris ?")

        c = create_contact(names, phone_number, is_favorite)
        add_contact(c)
        print(annuaire)


# c = create_contact("Théodule", "0646753956", True)
# add_contact(c)
# print(annuaire)
#
# c = create_contact("Océane", "0617010802", True)
# add_contact(c)
# print(annuaire)
#
# c = create_contact("Loïc", "0659222533", False)
# add_contact(c)
# print(annuaire)
#
# name = input("Nom du contact ?")
# if name == Theo:
#         print(Theo)
#
# if name == Oce:
#         print(Oce)
#
# if name == Lolo:
#         print(Lolo)
#
# newName = input("Entrez nom du nouveau contact :")
# print(newName)
# newNumber = input("Entrez numéro du nouveau contact :")
# print(newNumber)
# newFav = input("Voulez vous l'ajouter au favoris ?")
# print(newFav)
# add_contact(newName, newNumber, newFav)







