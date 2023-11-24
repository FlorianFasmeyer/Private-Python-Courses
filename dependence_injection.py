# L'injection de dépendance dans sa conception la plus simple est la possibilité de choisir (d'injecter) le comportement
# désiré dans une fonction (ou dans un object, mais nous verrons la POO plus tard). Cela se catégorise souvent par
# le fait de passer une fonction (le comportement) en paramètre, à une autre fonction qui en fera usage dans son code.

# L'injection de dépendances permet l'inversion des dépendances, un sujet que nous verrons plus tard. Il est néamoins
# important de noter que cette simple technique permet de "réutiliser" du code qui dépend en partie d'autres fonctions
# ou objets. En simple: L'injection de dépendances permet de réutiliser avec aise du code qui ne serait autrement pas
# réutilisable.

# L'exemple le plus simple pour les nouveaux sur Python :
def comportement_a(x):
    # Ne rien faire.
    return x


def comportement_b(x):
    # Multiplier par deux.
    return 2*x


def fonction(x, comportement):
    return f'le résultat de {comportement.__name__} pour la valeur {x} est {comportement(x)}.'


# Nous pouvons ainsi appeler la fonction et préciser le comportement à choix.
texte = fonction(10, comportement_b)
print(texte)


# Un exemple typique d'injection de dépendance est dans la fonction "login" sur un site web. Certains sites web
# proposent à l'utilisateur de s'enregistrer avec Google, Facebook our d'utiliser le système de login du site.
# Au lieu d'écrire trois différents codes implémentant le login, il suffit juste de spécifier les comportements.
def google_login(username, password):
    # fais quelque chose ...
    return True # retourne True si l'utilisateur se login avec success, False s'il y a un problème.


def facebook_login(username, password):
    # fais quelque chose ...
    return True # retourne True si l'utilisateur se login avec success, False s'il y a un problème.


def website_login(username, password):
    # fais quelque chose ...
    return True  # retourne True si l'utilisateur se login avec success, False s'il y a un problème.


def login(username, password, login_type):
    print('Hello and welcome to the login page.')
    print('Please wait for a response. Currently logging in...')
    result = login_type(username, password)
    if result is True:
        print('You successfully logged in! Well done!')
    else:
        print('Oh no, a problem occured!')


# Dans l'exemple ci-dessus, imaginons que la fonction login est bien plus complexe et fait une centaine de lignes.
# Dans ce cas l'usage de l'injection nous évite donc de réimplémenter ce code pour chaque type de login.
# Notons néamoins que pour que l'injection de dépendance fonctionne, toutes les fonctions de comportement doivent
# réagir de la même façon. input -> [username, password]; output-> [boolean] (True or False).


# Voici un example plus avancé. Nous définissons des fonctions à l'aide du lambda et utilisons un dictionnaire pour la
# sélection. Menu est la fonction utilisant des dépendances. Les lambdas sont les comportements, les dépendances.
# Tu remarqueras que cet exmple te sera bien utile lors de la conception de ton jeu Younes... ;)
rien, gauche, droite = lambda: print('fais rien!'), lambda: print('vas a gauche'), lambda: print('vas a droite')

options_dict = {
    'rien': rien,
    'gauche': gauche,
    'droite': droite
}


def menu(options):
    print('Veuillez choisir une option:')
    for option in options:
        print('\t', option)
        # \t pour tabulation.
        # \n pour à la line.
    while True:
        try:
            choice = input(':\> ')
            options[choice]()
            break
        except KeyError as err:
            print(err)


menu(options_dict)





