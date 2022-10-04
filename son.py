import pygame
import os


class Son: # Permet d'initialiser le son et la musique

    def __init__(self):
        self.ambiance = os.listdir("./son/ambiance")
        self.bruitage = {"pas": pygame.mixer.Sound("./son/bruitage/pas.wav"), "caisse":pygame.mixer.Sound("./son/bruitage/caisse.wav")}
        self.son = False
        self.volume_music = pygame.mixer.music.get_volume()
        self.vol_music = pygame.mixer.music
        self.vol_music.set_volume(0.5)
        pygame.mixer.music.fadeout(400)


    def play_ambiance(self): # Permet de lancer la playlist si le son est activer
        if self.son == True:
            for i in self.ambiance:
                if i == self.ambiance[0]:
                    pygame.mixer.music.load("./son/ambiance/"+i)
                pygame.mixer.music.queue("./son/ambiance/"+i)
            pygame.mixer.music.play()

    def play_bruitage(self, name): # Permet de lancer les bruitages que l'on demande
        """
        :param name: Prend la clé du bruit
        """
        self.bruitage[name].play()

    def Volume(self,up_down): # Permet de régler le volume de la musique
        """
        :param up_down: Indique si on monte (1) ou baisse (0) le son de la musique
        """
        a = self.volume_music
        if self.volume_music > 0 and up_down == 0:
            a -= 0.1

        if self.volume_music < 1 and up_down == 1:

            a += 0.1
        self.vol_music.set_volume(a)
        self.get_Volume()



    def activation(self): # Permet d'activer ou non la musique
        if self.son == True:
            self.son = False
            pygame.mixer.music.stop()
        else:
            self.son = True
            self.play_ambiance()

    def get_Volume(self): # Permet de d'actualiser le niveau sonore de la musique
        self.volume_music = pygame.mixer.music.get_volume()
