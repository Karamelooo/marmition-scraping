from utils.utils import send_marmiton_query

def nbr_ingredient_def():
    ingredient_is_setup = False
    while ingredient_is_setup is not True:
        try:
            nbr_ingredient = int(input('Combiens d\'ingrédient(s) voulez-vous utiliser ? '))
            ingredient_is_setup = True
        except ValueError:
            print('Veuillez écrire un nombre entier !')

    if nbr_ingredient == 0:
        print('Revenez une fois avoir acheté de quoi cuisiner !')
        exit()

    return nbr_ingredient

def temps_passe_recette():
    temps_passe_is_setup = False
    while temps_passe_is_setup is not True:
        try:
            temps_passe = int(input('Indiquez un temps de préparation en minute : '))
            if temps_passe > 0:
                temps_passe_is_setup = True
            else:
                print('Aucune recette ne peut durer 0 minute...')

        except ValueError:
            print('Veuillez écrire un nombre entier !')
    
    return temps_passe

def prix_recette():
    prix_is_setup = False
    while prix_is_setup is not True:
        try:
            prix = int(input('Indiquez le prix maximum de votre recette en euros : '))
            if prix > 0:
                prix_is_setup = True
            else:
                print('Aucune recette ne peut être gratuite...')

        except ValueError:
            print('Veuillez écrire un nombre entier !')

    if prix <= 8:
        prix = 1
    elif prix >= 10 and prix <= 20:
        prix = 2 
    else:
        prix = 3

    return prix


def difficulte_recette():
    difficulte_is_setup = False
    while difficulte_is_setup is not True:
        try:
            print('')
            print('''Très Facile (1)\nFacile (2)\nMoyen (3)\nDifficile (4)''')
            print('')
            difficulte = int(input('Indiquez une difficulté : '))
            difficulte_is_setup = True
        except ValueError or difficulte != 1 or difficulte != 2 or difficulte != 3 or difficulte != 4:
            print('Veuillez choisir une difficulté valide !')
    
    return difficulte


def main():
    try:
        filter_list = []

        # define le nombre d'ingrédient(s)
        ingredient_list = []
        nbr_ingredient = nbr_ingredient_def()
        for i in range(nbr_ingredient):
                ingredient_name = input(f"Entrez l'ingrédient numéro {i + 1}: ")
                ingredient_list.append(ingredient_name)

        filter_list.append({"ingredients": ingredient_list})

        # define le temps de passé en cuisine
        temps_passe = temps_passe_recette()
        filter_list.append({"temps_passe":temps_passe})

        # define le nombre de personne
        difficulte = difficulte_recette()
        filter_list.append({"difficulte":difficulte})

        # define le prix
        nbr_prix = prix_recette()
        filter_list.append({"nbr_prix":nbr_prix})
        
        recette_list = send_marmiton_query("-".join(filter_list[0]["ingredients"]),filter_list[3]["nbr_prix"],filter_list[2]["difficulte"],filter_list[1]["temps_passe"])

        # on recupère la list de recettes trouvées
        i = 1
        for recette in recette_list:
            print(f"-- RECETTE N°{i} --\n{recette['recette_name']} avec une note de {recette['recette_note']}\nVoir la recette : {recette['recette_link']}\n")
            i+=1

        
    except Exception as e:
        print("Une erreur s'est produite ! ",e)



main()