# _______________Creer_un_jeux video____________
import pygame
from pygame.locals import *
import math
import son
# ______________________________________________
# _______________Quitter import____________

# ______________________________________________
class Image(pygame.sprite.Sprite):  # Permet de creé les sprites
    def __init__(self, lien_image, position_x, position_y ):
        """
        :param lien_image:  Prends-le un lien d'image pour la load en tant que sprite
        :param position_x:  Prends une position x pou que le sprite à la même position x
        :param position_y:  Prends une position y pou que le sprite à la même position y
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(lien_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (position_x, position_y)
        self.width = self.image.get_width()




def menu_choix(NBCHOIX, choix, C, music): # Menu_position c'est pour d'elimiter la zone X, a
    """
    :param NBCHOIX: Prends le nombre de choix = au nombre de sprite dans C
    :param choix:   Prends le choix précédent pour la changer avec le choix actuel.
    :param C:       Prends le tableau des sprites affiché pour permettre la dectection de la souris dessus
    :param music:   Prends l'object music initialisé pour pouvoir l'activer/désactiver ou augmenter/réduire le son

    :return: Le choix sur lequel on est , si on veux quitter le menu, si on a choisi ou non.
    """
    valide = 0
    continuer = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pour quitter
            continuer = 0
            choix = "Quitter"

        # __________Choix par clavier________
        pygame.key.set_repeat(250, 200)
        if event.type == KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP or event.key == pygame.K_q:
                if choix == 0:
                    choix = NBCHOIX - 1
                else:
                    choix -= 1

            if event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_d:
                if choix == (NBCHOIX - 1):
                    choix = 0
                else:
                    choix += 1

            if event.key == pygame.K_x:
                music.Volume(0)
            if event.key == pygame.K_c:
                music.Volume(1)

        if event.type == KEYUP:
            if event.key == pygame.K_RETURN:
                valide = 1
            if event.key == pygame.K_ESCAPE:  # Pour quitter
                continuer = False
                choix = "Retour"
            if event.key == pygame.K_w:
                music.activation()


         # ______________________________________

        if event.type == MOUSEMOTION :
            for i in range(NBCHOIX):
                if (C[i].rect).collidepoint(event.pos):
                    choix = i

        if choix != "Retour" and choix != "Quitter":
            C[-1].rect = C[choix].rect

        if event.type == MOUSEBUTTONUP :
            for i in range(NBCHOIX):
                if (C[i].rect).collidepoint(event.pos):
                    valide = 1

    return [choix, continuer, valide]


def nbfichier(fenetre,chemin_menu,fond, coordonne, encardrer, choix_niveau, image, write, music):
    """
    :param fenetre: La fenetre du jeu pour rester sur la meme page
    :param chemin_menu: Tous les lien des boutons a clicker
    :param fond: Prend le lien , les coordonnées x et y dans un tableau pour chaque image de font
    :param coordonne: coordonne[0]: position x de départ ,coordonne[1]: position x * (la taille x du bouton + l'ecart entre les bouton/2), et coordonne[0]: position y de départ ,coordonne[1]: position y * (la taille y du bouton + l'ecart entre les bouton/2)
    :param encardrer: Représente le lien de l'image d'encadrement du choix
    :param choix_niveau: Représente le groupe de sprite de l'ancien menu
    :param image: Représente le lien de l'image des choix sans le texte
    :param write: True s'il doit écrire avec pygame le nom des niveaux sinon False
    :param music: Prends l'object music initialisé pour l'envoyer dans paramètre de commande

    :return:    Renvoie le lien du niveau ou sois indique qu'on veut quitter se menu
    """


    # ________Constante___________

    NBCHOIX = len(chemin_menu)

    # ____________________________
    # _________variable_______________
    choix = "Retour"
    continuer = 1
    # ________________________________


    a = []
    Texte = pygame.font.SysFont("Impact", 20)


    # Ajoute les image de fond au groupe de sprite
    if len(fond) != 0:
        for i in fond:
            image_fond = Image(i[0], i[1], i[2])
            choix_niveau.add(image_fond)
    # _____________________________________________

    reste = NBCHOIX

    # Permet d'afficher tout les boutons en ligne et cologne
    if reste < 4:
        cologne = reste
    else:
        cologne = 4

    if NBCHOIX != 0:
        choix = 0
        for j in range(math.ceil(NBCHOIX / cologne)):
            for i in range(cologne):
                Jouer = Image(image, coordonne[0] + (coordonne[1] * i), coordonne[2] + (coordonne[3] * j))
                choix_niveau.add(Jouer)
                a.append(Jouer)

            reste -= 4
            if reste < 4 :
                cologne = reste
    # ________________________________________________________

        
        Choix = Image(encardrer,  + coordonne[0], coordonne[2])
        choix_niveau.add(Choix)
        a.append(Choix)
        while continuer:
            # ___________________________________________________________________________



            # ________________Cela_permet_d'afficher_les _l'images_et_le_texte__________________________
            choix_niveau.draw(fenetre)
            if write :
                reste = NBCHOIX
                if reste < 4:
                    cologne = reste
                else: cologne = 4
                compte = 0
                for j in range(math.ceil(NBCHOIX / 4)):
                    for i in range(cologne):
                        texte = chemin_menu[compte].replace('.txt','') # mot egale ou inferieur a 13
                        niveau = Texte.render(texte, 1, (0, 0, 0))
                        fenetre.blit(niveau, (coordonne[0] + (coordonne[1] * i) +(75-len(texte)*4.75), coordonne[2] + (coordonne[3] * j) + 5))
                        compte += 1

                    reste -= 4
                    if reste < 4:
                        cologne = reste

            # ___________________________________________________________________________________________

            # ________________D'avoir_le_choix______________
            menu = menu_choix(NBCHOIX, choix, a, music)
            choix = menu[0]
            continuer = menu[1]
            # ______________________________________
            if menu[2] == 1:
                return chemin_menu[choix]

            del menu

            # ___________________________________________________________________________

            pygame.display.flip()
    return (choix)

def Cologne (fenetre,NBCHOIX,chemin_menu,fond,coordonne,encardrer, music):
    """"
    :param fenetre: La fenetre du jeu pour rester sur la meme page
    :param NBCHOIX: Le nombre de choix max du menu
    :param chemin_menu: Tous les lien des boutons a clicker
    :param fond: Prend le lien , les coordonnées x et y dans un tableau pour chaque image de font
    :param coordonne: coordonne[0]: position x ,coordonne[1]: position y + ecart entre les bouton/2, et coordonne[2]: position de depart = x * coordonne[1]
    :param encardrer: Représente le lien de l'image d'encadrement du choix
    :param music: Prends l'object music initialisé pour l'envoyer dans paramètre de commande

    :return: Le choix et le groupe de sprites pour si on en a besoin pour apres
    """

    # _________variable_______________
    continuer = 1
    choix = 0
    # ________________________________

    menue = pygame.sprite.Group()
    a = []
    # Ajoute les image de fond au groupe de sprite
    if len(fond) != 0:
        for i in fond:
            image_fond = Image(i[0], i[1], i[2])
            menue.add(image_fond)
    # _____________________________________________

    # Permet d'afficher tout les boutons en ligne et cologne
    for i in range(len(chemin_menu)):
        Jouer = Image(chemin_menu[i], coordonne[0], coordonne[1] * (coordonne[2] + i))
        menue.add(Jouer)
        a.append(Jouer)
    Choix = Image(encardrer, coordonne[0], coordonne[1] * coordonne[2])
    menue.add(Choix)
    a.append(Choix)
    # ___________________________________________________________________________

    while continuer:


        # ___________________Cela_permet_d'afficher_les__l'images____________________________________
        menue.draw(fenetre)
        # ___________________________________________________________________________________________

        # ___________________Choix______________
        menu = menu_choix(NBCHOIX, choix, a, music)
        choix = menu[0]
        continuer = menu[1]
        # ______________________________________


        if menu[2] == 1:
            return [choix, menue]
        del menu


        pygame.display.flip()
    return [choix, menue]





