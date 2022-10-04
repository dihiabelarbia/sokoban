
def save(save):
        tableau = []
        #Création d'un nouveau tableau pour réécrire dedans.
        with open("./Sauvegarde/Save.txt", "w") as file:
                #ouverture du fichier pour pouvoir écrire.
                for ligne in save:
                        #Lecture ligne par ligne du tableau.
                        a = ("-".join(ligne))
                        #Mettre les tirets entre les chiffres.
                        file.write(a)
                        #Écriture dans le fichier.

               
#la touche de sauvegarde sera dans le programme principal.


