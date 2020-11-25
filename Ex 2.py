import math as ma


def first_test(n):
    """ test naïf de primalité
    retourne True si l'entier est premier, et inversement
    n : un entier naturel
    """
    for a in range(2, int(ma.sqrt(n))):
        if n % a == 0:
            return False
    return True


def pi(x):
    """retourne le nombre de premiers inférieurs à x
    X : un réel
    """
    cpt = 0
    for n in range(1, int(x)):
        if first_test(n):
            cpt += 1
    return cpt


def gen_carmicheal(t):
    """retourne tous les nombres de Carmichael inférieurs à x
    t : un réel
    """
    res = []
    for x in range(3, int(t), 2):  # les nombres de Carmichael sont impairs
        if x % 1000 == 1:
            print(x)
        valid = False
        for y in range(2, x):
            if ma.gcd(x, y) == 1:
                if pow(y, x-1, x) != 1:
                    valid = False
                    break
            else:
                valid = True
        if valid:
            res.append(x)

    return res


def gen_carmicheal(a, b, c):
    """ genère un nombre de Carmicheal à partir de trois diviseurs premiers"""

# pi(1e5) = 9680
# gen_carmicheal(1e5) = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745,
# 63973, 75361]

