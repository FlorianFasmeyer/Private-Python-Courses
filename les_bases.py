# Les bases de la programmation.
# Compatible avec tous les languages.


# 1. Un code "Turing complete"
# La programmation nécessite trois principes fondateurs pour être considéré comme Turing complete (capable de tout).
# La séquence, la sélection et l'itération!
# "The game of life", un jeu par Conway, est dit Turing complete, car l'on peut implémenter des ordinateurs,
# languages de programmation et même implémenter "the game of life" dans "the game of life".
# C'est quoi le "game of life"?: https://www.youtube.com/watch?v=C2vgICfQawE&t=9s
# Implémentation du "game of life" dans le "game of life" avec de multiples inceptions:
#     https://www.youtube.com/watch?v=4lO0iZDzzXk

# Le système de redstone dans Minecraft est lui aussi Turing complete, car l'on peut, en théorie du moins, implémenter
# la totalité de Minecraft avec Minecraft. L'on peut aussi créer des ordinateurs dans Mineract! L'on peut aussi
# implémented Conway's game of life dans Minecraft et inversément.
# Minecraft dans Minecraft : https://www.youtube.com/watch?v=-BP7DhHTU-I
# The game of life dans Minecraft: https://www.youtube.com/watch?v=D8FMiFswZN8


# 1.1 La séquence.
# Le code s'active une ligne après l'autre.
a = 10      # 1.
b = 20      # 2.
c = a + b   # 3.
print(c)    # 4.

# 1.2 La sélection.
# Il est possible de choisir le chemin du code. D'utiliser du code pour sélectionner quelle partie du code va être
# lue et quelle partie peut être ignorée.
if c > 15:
    print('C is greater than 15')
elif c < 10:  # elif en python est appelé "else if" dans les autres languages comme le C.
    print('C is smaller than 10')
else:
    print('C is between 10 and 15')

# 1.3 L'itération (la boucle, la répétition).
my_dogs = ('milou', 'scooby doo', 'johny jumper')
for dog in my_dogs:
    print(f'{dog} is my dog.')


# 2. Les fonctions
# Les fonctions ont multiples entrées (attributs)
# mais une seule sortie (return).

# Créons la fonction f(x) = x et g(x, y) = x + y
def f(x):
    return x


# Deux entrées, une seule sortie.
def g(x, y):
    return x + y


# Utilisation des fonctions:
# Note: Print() est une fonction pour afficher les résultats.
print(f(1))
print(g(5, 4))

# Nous pouvons utiliser le résultat des fonctions pour faire des maths.
resultat = 2 * f(3)
print(resultat)  # Affiche 6.
resultat2 = f(10) + f(5, 2)
print(resultat2)  # Affiche 17.


# 3. Le contexte.
#     L'on peut appeler une variable globale de partout.
#     L'on peut appeler une variable de son propre contexte ou d'un contexte englobant.

# Contexte: Global.
variable_globale = 'je suis globale'


def fonction():
    # Contexte: function()
    variable_local = 'je suis locale à function'

    def fonction_interne():
        # Contexte: function_interne()
        variable_inception = 'je suis locale à function_interne()'
        print(variable_globale)  # ça marche!
        print(variable_local)  # ça marche!
        print(variable_inception)  # ça marche!
        # function()  # ça marche, mais ça crash! <- C'est de la récursion! nous verrons ça plus tard...
        # fonction_interne()  # ça marche, mais ça crash! <- C'est de la récursion! nous verrons ça plus tard...
        # On sort du contexte de fonction_interne()...

    # Contexte: function().
    print(variable_globale)  # ça marche!
    print(variable_local)  # ça marche!
    # print(variable_inception) # ça marche PAS! variable_inception n'existe que dans fonction_interne().
    # function()  # ça marche, mais ça crash! <- C'est de la récursion! nous verrons ça plus tard...
    fonction_interne()  # ça marche!
    # On sort du contexte de fonction()...


# Contexte: global.
print(variable_globale)  # ça marche!
# print(variable_local) # ça marche PAS! variable_blobale n'existe que dans fonction()
# print(variable_inception) # ça marche PAS! variable_inception n'existe que dans fonction_interne()
fonction()  # ça marche!
# fonction_interne() # ça marche PAS!

# Note: variable_globale et fonction() sont déclarés dans le contexte global.


# L'idée de "contexte" en programmation est proche du "contexte" en français. Dans le contexte de déplacement en
# voiture, "vitesse" se réfère généralement à la vitesse en kilomètres par heures (30km/h) alors qu'en developement
# software, la vitesse peut se référer à la rapiditée avec laquelle un developeur créé du code pour résoudre un
# problème ou si l'on parle du temps nécessaire à afficher le résultat, du temps d'exécution du code en millisecondes.
def programmation():
    def developpement_software():
        vitesse = 10  # Le dévelopeur ajoute lignes de code par seconds à son code.

    def execution_du_code():
        vitesse = 100  # Le software prend 100 millisecondes pour s'exécuter.


def voitures():
    vitesse = 200  # La voiture se déplace à 200km/h!