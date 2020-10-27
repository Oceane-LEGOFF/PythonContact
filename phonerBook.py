import logger



def create_contact(names, phone_number, is_favorite):
    """
    Creer un contact
    :param names: Son nom
    :param phone_number: Son numéro
    :param is_favorite: Si il est en favoris
    :return: Le contact
    """
    contact = {
        "names": names,
        "phone_number": phone_number,
        "is_favorite": is_favorite,
    }
    return contact

annuaire = {}
#creer un dictionnaire de contacts


def add_contact(new):
    """
    Ajoute un contact
    :param: new
    :return: Information du nouveau contact
    """
    logger.ecrire_fichier("Ajout du contact " + new["names"])
    phone_number = new["phone_number"]
    annuaire[phone_number] = new

    # trier nom par ordre alphabetique


def get_names(n):
    """
    Reccupere nom du contact
    :param: n
    :return: Nom du nouveau contact
    """
    names = n["names"]
    annuaire[get_names] = n
    return names


def get_number(c):
    """
    Reccupere numéro du contact
    :param: c
    :return: Numéro du contact
    """
    phone_number = c["phone_number"]
    annuaire[phone_number] = c
    return phone_number


def get_fav(f):
    """
    Reccupere information si le contact est dans les favoris ou non
    :param: f
    :return: Si le contact est dans les favoris ou non
    """
    favoris = f["favoris"]
    annuaire[get_fav] = f
    return favoris


