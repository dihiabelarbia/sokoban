import pygame
import menu
import time
import affiche
import Sauvegarde.Sauvegarde
import son
pygame.init()


class player(pygame.sprite.Sprite):
    def __init__(self, spawn):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.deplacement_pixels = 5
        # __________initialiser l'image du depart_____________
        self.image = pygame.image.load('./image/personnage/perso_bas.png')
        # __________recuperer la positioon du joueur__________
        self.rect = self.image.get_rect()
        # __________initialiser la position du joueur_________
        self.rect.x = spawn[0] + 14
        self.rect.y = spawn[1]
        self.game = True
        self.move = 0
        self.bruitage = son.Son()
        self.music = son.Son()
        self.choix = 0



    def deplacement(self, fenetre, niveau, option, sprite_nomove, caisse, sorti, tab, all_sprite, music):
        """
        :param fenetre: La fenetre du jeu pour rester sur la meme page
        :param niveau: Le lien du niveau sur lequel on joue
        :param option: Le sprite engrenage pour lancer le menu du jeu
        :param sprite_nomove: Le tableau des sprites affiché
        :param caisse: Le tableau des sprites caisse que l'on peut bouger
        :param sorti: Le  sprite de sortit pour vérifier si vous avais fini
        :param tab: Le tableau du niveau
        :param all_sprite: Le groupe de sprite qui contien tout les sprites
        :param music: Prends l'object music initialisé pour l'envoyer dans paramètre de commande
        """
        self.sprite_nomove = sprite_nomove
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                self.game = False
                self.choix = "Quitter"
            pygame.key.set_repeat(100, 40)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:        # Déplacement vers le bas = 0
                    if self.move == 3: # pour rectifier la différence de largeur
                        self.rect.x -= 5
                    self.image = pygame.image.load('./image/personnage/perso_bas.png')
                    self.move = 0
                    self.rect.size = (26, 46)                                   # Permet de rectifier la surface de l'image
                    if self.colision(self, sprite_nomove) != True:
                        self.rect.y += self.deplacement_pixels

                if event.key == pygame.K_UP or event.key == pygame.K_z:          # Déplacement vers le haut = 2
                    if self.move == 3: # pour rectifier la différence de largeur
                        self.rect.x -= 5
                    self.image = pygame.image.load('./image/personnage/perso_haut.png')
                    self.move = 2
                    self.rect.size = (26, 46)                                     # Permet de rectifier la surface de l'image
                    if self.colision(self,sprite_nomove) != True:
                        self.rect.y -= self.deplacement_pixels

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # Déplacement vers la droite = 3
                    self.move = 3
                    self.image = pygame.image.load('./image/personnage/perso_droite.png')
                    self.rect.size = (13, 46)                               # Permet de rectifier la surface de l'image
                    if self.colision(self,sprite_nomove) != True:
                        self.rect.x += self.deplacement_pixels

                if event.key == pygame.K_LEFT or event.key == pygame.K_q:   # Déplacement vers la gauche = 1
                    self.image = pygame.image.load('./image/personnage/perso_gauche.png')
                    self.move = 1
                    self.rect.size = (13, 46)                               # Permet de rectifier la surface de l'image
                    if self.colision(self,sprite_nomove) != True:
                        self.rect.x -= self.deplacement_pixels

                if event.key == pygame.K_x:                                 # Baisse le son de la musique
                    music.Volume(0)
                if event.key == pygame.K_c:                                 # Augmente le son de la musique
                    music.Volume(1)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_e:                             # Permet de lancer les animations
                    move_caisse = self.animation(caisse)
                    fin = self.animation(sorti)
                    if move_caisse != None :                            # Permet de faire avancer la caisse devant nous
                        for x in range(move_caisse.width):
                            if self.colision(move_caisse, self.sprite_nomove) != True:
                                self.bruitage.play_bruitage("caisse")
                                if self.move == 2:
                                    move_caisse.rect.y -= 0.1
                                    self.rect.y -= 0.1
                                elif self.move == 0:
                                    move_caisse.rect.y += 1
                                    self.rect.y += 1
                                elif self.move == 1:
                                    move_caisse.rect.x -= 1
                                    self.rect.x -= 1
                                elif self.move == 3:
                                    move_caisse.rect.x += 1
                                    self.rect.x += 1
                                all_sprite.draw(fenetre)
                                fenetre.blit(self.image, self.rect)
                                pygame.display.flip()

                    if fin != None :                                    # Permet de vérifier si vous avais fini et active le menu de fin

                        if affiche.gagner(affiche.tableau1(fenetre, tab, caisse, self)) != False:

                            chemin = ["./image/clic/menu/menu_principal.png","./image/clic/menu/quitter.png"]
                            nbchoix = 2
                            [choix, poubelle] = menu.Cologne(fenetre, nbchoix, chemin, [], [fenetre.get_width() / 3, fenetre.get_height() / 10, 3.5], "./image/clic/menu/choix.png", music)

                            if choix == 0:
                                self.choix = "Retour"
                                self.game = False
                            elif choix == 1:
                                self.choix = "Quitter"
                                self.game = False

                if event.key == pygame.K_w:                             # Permet d'activer ou désactiver la music
                    music.activation()

                if event.key == pygame.K_ESCAPE:                        # Permet de lancer le menu du jeu

                    if niveau != "./Sauvegarde/Save.txt":
                        chemin = ["./image/clic/menu/jouer.png","./image/clic/menu/new_game.png", "./image/clic/menu/option.png",
                    "./image/clic/menu/quitter.png"]
                        nbchoix = 4
                    else:
                        chemin = ["./image/clic/menu/jouer.png",
                                  "./image/clic/menu/option.png",
                                  "./image/clic/menu/quitter.png"]
                        nbchoix = 3
                    [choix, poubelle] = menu.Cologne(fenetre, nbchoix, chemin, [],[fenetre.get_width() / 3, fenetre.get_height() / 10, 3.5],"./image/clic/menu/choix.png", music)

                    if niveau != "./Sauvegarde/Save.txt":
                        if choix == 1:
                            self.choix = "Recommencer"
                            self.game = False
                        elif choix == 2:
                            continuer2 = True
                            while continuer2:
                                for event2 in pygame.event.get():
                                    if event2.type == pygame.QUIT:
                                        continuer2 = False
                                        Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                                        self.game = False
                                        self.choix = "Quitter"
                                    if event2.type == pygame.KEYUP:
                                        if event2.key == pygame.K_ESCAPE:
                                            continuer2 = False
                                image_options = pygame.image.load("./image/fond/menu/options.png").convert()
                                fenetre.blit(image_options, (0, 0))
                                pygame.display.flip()


                        elif choix == 3:
                            Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                            self.game = False
                    else:
                        if choix == 1:
                            continuer2 = True
                            while continuer2:
                                for event2 in pygame.event.get():
                                    if event2.type == pygame.QUIT:
                                        continuer2 = False
                                        Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                                        self.game = False
                                        self.choix = "Quitter"
                                    if event2.type == pygame.KEYUP:
                                        if event.key == pygame.K_ESCAPE:
                                            continuer2 = False
                                image_options = pygame.image.load("./image/fond/menu/options.png").convert()
                                fenetre.blit(image_options, (0, 0))
                                pygame.display.flip()
                        elif choix == 2:
                            Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                            self.game = False



            if event.type == pygame.MOUSEBUTTONUP:                      # Permet de lancer le menu du jeu avec la souris
                if (option.rect).collidepoint(event.pos):
                    if niveau != "./Sauvegarde/Save.txt":
                        chemin = ["./image/clic/menu/jouer.png", "./image/clic/menu/new_game.png",
                                  "./image/clic/menu/option.png",
                                  "./image/clic/menu/quitter.png"]
                        nbchoix = 4
                    else:
                        chemin = ["./image/clic/menu/jouer.png",
                                  "./image/clic/menu/option.png",
                                  "./image/clic/menu/quitter.png"]
                        nbchoix = 3
                    [choix, poubelle] = menu.Cologne(fenetre, nbchoix, chemin, [],
                                                     [fenetre.get_width() / 3, fenetre.get_height() / 10, 3.5],
                                                     "./image/clic/menu/choix.png", music)

                    if choix == 0:
                        pass
                    if niveau != "./Sauvegarde/Save.txt":
                        if choix == 1:
                            self.choix = "Recommencer"
                            self.game = False
                        if choix == 2:
                            pass


                        elif choix == 3:
                            Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                            self.game = False
                    else:
                        if choix == 1:
                            pass


                        elif choix == 2:
                            Sauvegarde.Sauvegarde.save(affiche.tableau1(fenetre, tab, caisse, self))
                            self.game = False


    def colision(self,joueur,g_p):
        for i in g_p:
            if self.move == 2:
                if joueur.rect.top > i.rect.top and joueur.rect.top < i.rect.bottom and joueur.rect.right -10 > i.rect.left and joueur.rect.left+2 < i.rect.right:
                    return True
            elif self.move == 0:
                if joueur.rect.bottom < i.rect.bottom and joueur.rect.bottom > i.rect.top and joueur.rect.right-10 > i.rect.left and joueur.rect.left+2 < i.rect.right:
                    return True
            elif self.move == 1:
                if joueur.rect.left > i.rect.left and joueur.rect.left < i.rect.right and joueur.rect.bottom - 5 > i.rect.top and joueur.rect.top + 5 < i.rect.bottom:
                    return True
            elif self.move == 3:
                if joueur.rect.right > i.rect.left and joueur.rect.right < i.rect.right and joueur.rect.bottom - 5 > i.rect.top and joueur.rect.top + 5 < i.rect.bottom:
                    return True


    def animation(self,caisse): # Vérifie s'il y a un sprite qui active une animation devant le player

        """
        :param caisse: Prends le tableau qui posséde des sprites pour vérifier si vous pouvez lancer l'animation
        :return: Renvoye le sprite a animer ou rien
        """

        for i in caisse:
            if self.move == 2 :
                if self.rect.centerx >= i.rect.topleft[0] and self.rect.centerx <= i.rect.topright[0] and self.rect.top+1 >= i.rect.topleft[1] and self.rect.top-1 <= i.rect.bottomright[1]:
                    return i

                            # animation haut
            if self.move == 0 :
                if self.rect.centerx >= i.rect.topleft[0] and self.rect.centerx <= i.rect.topright[0] and self.rect.bottom+1 >= i.rect.topleft[1] and self.rect.bottom-1 <= i.rect.bottomright[1]:
                    return i
                            # animation bas

            if self.move == 1 :
                if self.rect.left+1 >= i.rect.topleft[0] and self.rect.left-1 <= i.rect.topright[0] and self.rect.centery >= i.rect.topleft[1] and self.rect.centery <= i.rect.bottomright[1]:
                    return i
                        # animation gauche

            if self.move == 3 :
                if self.rect.right+1 >= i.rect.topleft[0] and self.rect.right-1 <= i.rect.topright[0] and self.rect.centery >= i.rect.topleft[1] and self.rect.centery <= i.rect.bottomright[1]:
                    return i
                            # animation droite