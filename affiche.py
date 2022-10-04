# _______________Creer_un_jeux video____________
import pygame
import math
# ______________________________________________
# _______________________________________________
import deplacement
import menu



Image = menu.Image


# Utilisation de classes pour creer les sprites




'''Ancienne méthode d'affichage des images (toujours utilisée pour le fond d'écran)
fenetre = la fenetre qu'on a créée; image = chemin pour l'image d'origine'''

def Ajeu(niveau, music):
    music.play_ambiance()
    continuer = 1
    pygame.init()
    # ________Constante___________
    TAILLE = [1024, 768]

    # __________________________Initialise_la_fenetre____________________________
    fenetre = pygame.display.set_mode((TAILLE))  # creer_la_page
    pygame.display.set_caption("Sokoban")  # Nom_du_jeu

    # ___________________________________________________________________________
    all_sprite = pygame.sprite.Group()
    sprite_nomove = []
    caisse = []
    sorti = []

    # _________variable_position_______________
    position_x = (fenetre.get_width() / 3.5)

    # ______________________________Fond_______________________________________________

    spawn = [0, 0]
    pixelx = 50
    pixely = 50

    x = 0
    y = 0

    xposition = x * pixelx  # position x d'affichage
    yposition = y * pixely  # poisiton y d'affichage
    font = Image("./image/fond/menu/wall.jpg", 0, 0 )
    all_sprite.add(font)
    font = Image("./image/niveau/sol.png", (xposition + position_x), (yposition + (fenetre.get_height() / 5)))
    all_sprite.add(font)
    option = Image("./image/clic/menu/engrenage.png", 0,0)
    all_sprite.add(option)

    with open(niveau, "r") as j:
        tableau = []
        for ligne in j:
            tableau.append(ligne.split("-"))
        for ligne_y in tableau:

            # position y d'affichage
            yposition = (y * pixely) + (fenetre.get_height() / 5)
            for ligne_x in ligne_y:
                # position x d'affichage
                xposition = (x * pixelx) + position_x
                ligne_x = int(ligne_x)
                ''' En fonction des valeurs récupérées dans le tableau niveau.txt, 
                    nous renvoyons les coordonnés x et y ainsi que le lien vers l'image
                    à charger dans le sprite à la class Image qui affichera le Sprite'''
                if int(ligne_x) == 0:
                    block = Image("./image/niveau/mur.png", xposition, yposition)
                    sprite_nomove.append(block)
                elif int(ligne_x) == 1:
                    if int(tableau[y][x - 1]) == 3 or int(tableau[y][x + 1]) == 3 or int(
                            tableau[y - 1][x]) == 3 or int(tableau[y + 1][x]) == 3:
                        if niveau != "./Sauvegarde/Save.txt":
                            spawn[0] = xposition
                            spawn[1] = yposition + 1
                elif int(ligne_x) == 2:
                    boite = Image("./image/niveau/caisse.png", xposition, yposition)
                    sprite_nomove.append(boite)
                    caisse.append(boite)
                elif int(ligne_x) == 3:
                    block = Image("./image/niveau/entree.png", xposition, yposition)
                    sprite_nomove.append(block)
                elif int(ligne_x) == 4:
                    block = Image("./image/niveau/sortie.png", xposition, yposition)
                    sprite_nomove.append(block)
                    sorti.append(block)
                elif int(ligne_x) == 5:
                    block = Image("./image/niveau/Stockage.png", xposition, yposition)
                all_sprite.add(block)

                if int(ligne_x) == 6:
                    spawn[0] = xposition
                    spawn[1] = yposition + 1
                x += 1
            y += 1
            x = 0
    for i in caisse:
        all_sprite.add(i)
    player = deplacement.player(spawn)


    while continuer:

        player.deplacement(fenetre, niveau, option, sprite_nomove, caisse, sorti, tableau, all_sprite, music)
        continuer = player.game
        all_sprite.draw(fenetre)
        fenetre.blit(player.image, player.rect)
        pygame.display.flip()
    if player.choix == "Quitter":
        return "Quitter"
    elif player.choix == "Retour":
        return "Retour"
    elif player.choix == "Recommencer":
        Ajeu(niveau,music)


def tableau1(fenetre, tab1, caisse, positionJ):
    """

    :param fenetre: La fenetre pygame qu'on a deja lancé
    :param tab1: Le tableau du niveau lancé
    :param caisse: Tableau qui comprend tout les sprites caisses
    :param positionJ: La position du joueur
    :return: Le tableau niveau avec dedans la position actualiser du joueur et des caisses
    """
    tab =  [i.copy() for i in tab1]
    for j in range(len(tab)):
        for k in range(len(tab)):
            if tab[j][k] == " 2 ":
                tab[j][k] = " 1 "
            if tab[j][k] == " 6 ":
                tab[j][k] = " 1 "

    for i in caisse:
        tab[math.floor((i.rect.centery-(fenetre.get_height() / 5))/50)][math.ceil((i.rect.centerx - (fenetre.get_width() / 3))/50)] = " 2 "
    tab[math.floor((positionJ.rect.centery - (fenetre.get_height() / 5)) / 50)][math.ceil((positionJ.rect.centerx - (fenetre.get_width() / 3)) / 50)] = " 6 "
    return(tab)

def gagner(tableau):
    """
    :param tableau: Prend un tableau
    :return: Renvoie False si il y a un " 5 " dans le tableau
    """
    for i in tableau:
        if (" 5 " in i):
            return False