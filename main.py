import sys
import phonerBook


# from art import *
# print(text2art("CONTACT", font="block"))


args = sys.argv
for i in range(0, len(args)):
    if args[i] == "-log":
        print("Il est present")


programme = True
while programme:
#boucle qui premet de poser plusieurs fois les questions, pour pouvoir entrer plusieurs contacts
        names = input("Entrez nom du nouveau contact :")
        phone_number = input("Entrez numero du nouveau contact :")
        is_favorite = input("Voulez vous l'ajouter en Favoris ?")

        c = phonerBook.create_contact(names, phone_number, is_favorite)
        phonerBook.add_contact(c)
        print(phonerBook.annuaire)