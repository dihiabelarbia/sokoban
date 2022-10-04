import pygame
import affiche
import menu
import os
import son



if __name__ == '__main__':
    continuer = True
    leave = ""
    pygame.init()
    TAILLE = [1024, 768]
    # __________________________Initialise_la_fenetre____________________________
    # icone
    icon = pygame.image.load("./image/personnage/icon.png")
    pygame.display.set_icon(icon)
    # _____

    fenetre = pygame.display.set_mode((TAILLE))  # creer_la_page
    pygame.display.set_caption("Sokoban")  # Nom_du_jeu

    # _______________Creer_et_lance_la_musique______________
    music = son.Son()
    music.play_ambiance()
    # ______________________________________________________

    # ___________________________________________________________________________

    # __________________________Menu-Principal____________________________
    while continuer or leave:
        music.play_ambiance()
        continuer1 = True

        # ___________________________Affichage__________________________
        [choix,poubelle] = menu.Cologne(fenetre, 5, ["./image/clic/menu/jouer.png", "./image/clic/menu/new_game.png",
                   "./image/clic/menu/option.png", "./image/clic/menu//credit.png",
                   "image/clic/menu/quitter.png"],
                      [["./image/fond/menu/wall.jpg", 0, 0], ["./image/fond/menu/titre.png", fenetre.get_width()/4, 70]], [fenetre.get_width()/3, fenetre.get_height() / 10, 3.5], "./image/clic/menu/choix.png",music)
        # _______________________________________________________________

        # ____________________Lance_le_jeu_avec_la_sauvegarde________________________________
        if choix == 0 :
            jeu = affiche.Ajeu("./Sauvegarde/Save.txt",music)
            if jeu == "Quitter":
                continuer = False
        # ___________________________________________________________________________________

        # _______________________________Second_Menu___________________________________
        elif choix == 1:

            while continuer1 :
                music.play_ambiance()
                continuer = True

                # ___________________________Affichage__________________________
                [choix2, sprite] = menu.Cologne(fenetre, 2, ["./image/clic/menu/campagne.png", "./image/clic/menu/creation.png"],
                      [["./image/fond/menu/wall.jpg", 0, 0], ["./image/fond/menu/choix_typeLV.jpg", 0, 0]], [20, 55, 2], "./image/clic/menu/choix2.png",music)
                # _______________________________________________________________

                # _______________Choix_de_niveaux_____________
                if choix2 == 0:

                    # ___________________________Affichage__________________________
                    niveau = menu.nbfichier(fenetre, os.listdir("./niveau/campagne"), [["image/fond/menu/niveaux.png", fenetre.get_width() / 4, 2]], [fenetre.get_width() / 3.5, 155, fenetre.get_height() / 6, 38], "./image/clic/menu/choix3.png", sprite, "./image/clic/menu/test.png", True, music)
                    # _______________________________________________________________

                    # ___________________Pour_quiter_ou_revenir_en_arriere_________________
                    if niveau == "Retour":
                        pass
                    elif niveau == "Quitter":
                        continuer = False
                        continuer1 = False
                    # ______________________________________________________________________

                    # ___________________Lancer_le_niveau_choisi____________________________
                    else:
                        niveau = affiche.Ajeu(f"./niveau/campagne/{niveau}", music)
                        if niveau == "Retour":
                            continuer1 = False
                        elif niveau == "Quitter":
                            continuer = False
                            continuer1 = False
                    # ______________________________________________________________________

                # ____________________________________________

                # _______________Choix_de_niveaux_ personaliser_____________
                elif choix2 == 1:
                    niveau = menu.nbfichier(fenetre, os.listdir("./niveau/personaliser"), [["image/fond/menu/niveaux.png", fenetre.get_width() / 4, 2]], [fenetre.get_width() / 3.5, 155, fenetre.get_height() / 6, 38],
                                            "./image/clic/menu/choix3.png", sprite, "./image/clic/menu/test.png", True, music)

                    if niveau == "Retour":
                        pass
                    elif niveau == "Quitter":
                        continuer = False
                        continuer1 = False
                    else:
                        affiche.Ajeu(f"./niveau/personaliser/{niveau}", music)

                # __________________________________________________________


                # ___________________Pour_quiter_ou_revenir_en_arriere_________________
                elif choix2 == "Retour":
                    continuer1 = False
                elif choix2 == "Quitter":
                    continuer = False
                    continuer1 = False
                # ______________________________________________________________________
        # __________________________________________________________________________________

        # _______________________________Les_touches_utilisables___________________________________
        elif choix == 2:
            continuer2 = True
            while continuer2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continuer2 = False
                        continuer1 = False
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            continuer2 = False
                image_options = pygame.image.load("./image/fond/menu/options.png").convert()
                fenetre.blit(image_options, (0,0))
                pygame.display.flip()
        # _________________________________________________________________________________________

        # __________________________________Les_crédits___________________________________________
        elif choix == 3 :
            continuer2 = True
            while continuer2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continuer2 = False
                        continuer1 = False
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            continuer2 = False
                image_credit = pygame.image.load("./image/fond/menu/credits.png").convert()
                fenetre.blit(image_credit, (0, 0))
                pygame.display.flip()

        # _________________________________________________________________________________________

        # __________________________________Fermer_la_fenetre______________________________________
        elif choix == 4 or choix =="Quitter" or choix == "Retour" or leave == False:
            continuer = False
        # _________________________________________________________________________________________
    # ___________________________________________________________________