# coding: utf8
# chargement des fonctionalité d'image ainsi que de low et high
from stegano import *

# charge le fichier
size, image = image_load('message_x.png')

# crée une nouvelle image de résultat
result = image_new(size)

# ici votre code de decodage
...

# sauvegarde l'image
image_save(result, size, 'resultat.png')
