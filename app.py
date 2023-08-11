from utils.utils import send_marmiton_query
import pygame
from pygame import *
from io import BytesIO
from urllib.request import urlopen
import webbrowser
import math

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
                ingredient_is_setup = False
                while ingredient_is_setup is False:
                    ingredient_name = input(f"Entrez l'ingrédient numéro {i + 1}: ")
                    if ingredient_name != "" and ingredient_name != " ":
                        ingredient_list.append(ingredient_name)
                        ingredient_is_setup = True
                    else:
                        print('Veuillez renseigner un ingrédient !')

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


        recette_displayed = False
        scroll = False

        # initiation pygame pour afficher les résultats
        pygame.init()

        ctx_width = 800
        ctx_height = 600
        nb = 0
        step = 4
        total = len(recette_list)
        ctx = pygame.display.set_mode((ctx_width, ctx_height))
        pygame.display.set_caption(f"{total} recettes trouvées")
        verdana = pygame.font.match_font('verdana')
        wingdings = pygame.font.match_font('wingdings2')
        font = pygame.font.Font(verdana, 11)
        font_stars = pygame.font.Font(wingdings, 17)
        running = True
        links = []
        pos_y = []
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and scroll is False:
                    scroll = True
                    if event.button == 4 and nb > 0:
                        nb -= step
                    elif event.button == 5 and nb < total:
                        nb += step
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(event.pos) #coordonnées du clique
                    n_link = 0
                    for p in pos_y:
                        if event.pos[1] >= p and event.pos[1] < p+45:
                            print(p)
                            webbrowser.open(links[n_link])
                            break
                        n_link+=1

            # génération de l'image
            ctx.fill((235, 235, 235))
            x,y = (0,0)
            w_rect = 100
            h_rect = 40
            rect_color = (100,100,100)
            border_color = (0,0,0)
            txt_color = (30,30,30)
            stars_color = (255,0,0)
            blank_stars_color = (0,0,0)
            border_size = 1
            # génération des recettes trouvées
            if(recette_displayed is False or scroll is True):
                links = []
                pos_y = []
                if(nb+15 > total):
                    max_i = total
                else:
                    max_i = nb+15
                for index in range(nb, max_i):
                    recette = recette_list[index]
                    links.append(recette['recette_link'])
                    pos_y.append(y)

                    response = urlopen(recette['recette_image']).read()
                    image = BytesIO(response)
                    image = pygame.image.load(image)
                    image = pygame.transform.scale(image, (100, 40))
                    note = recette['recette_note'].split('/')
                    note = math.floor(float(note[0]))
                    stars = ""
                    blank_stars = ""
                    for star in range(0, note):
                        stars += "ê"
                    for ok in range(0, 5-note):
                        blank_stars += "ê"
                    title = f"""-- RECETTE N°{index+1} --"""
                    texte = f"""
{recette['recette_name']} avec une note de {recette['recette_note']}
Cliquez pour accéder à la recette

"""
                    # rectangle + bordure
                    pygame.draw.rect(ctx, rect_color, (x, y, w_rect, h_rect))
                    pygame.draw.rect(ctx, border_color, (x - border_size, y - border_size, w_rect + 2 * border_size, h_rect + 2 * border_size), border_size)
                    pygame.draw.rect(ctx, border_color, (x - border_size, y - border_size, 1000 + 2 * border_size, h_rect + 2 * border_size), border_size)
                    # affichage de l'image dans le rectangle si existante
                    ctx.blit(image, (x, y))
                    # génération du texte
                    y+=5
                    surface_texte = font.render(title, True, txt_color)
                    ctx.blit(surface_texte, (105, y))
                    surface_texte = font_stars.render(stars, True, stars_color)
                    x_stars = ctx.blit(surface_texte, (220, y)).right
                    surface_texte = font_stars.render(blank_stars, True, blank_stars_color)
                    ctx.blit(surface_texte, (x_stars, y))
                    for ligne in texte.splitlines():
                        surface_texte = font.render(ligne, True, txt_color)
                        ctx.blit(surface_texte, (105, y))
                        pygame.display.flip()
                        y+=10
                y+=10
            recette_displayed = True
            scroll = False

        pygame.quit()
        
    except Exception as e:
        print("Une erreur s'est produite ! ",e)

main()