# -*- coding: utf-8 -*-
"""

@author: christ bohou
"""

from fltk import *
from time import sleep
import random


################################################################################################################ tache01 ########################################

def case_vers_pixel(
        sommet):  # avec sommet qui a i et j comme coordonnéés , ceci est bien definit dans la ligne qui suis

    """

    cette fontion a pour but de convertir les coordonnées du sommet en coordonnées PIXEL  et ça en prenant comme paramettre (sommet)du plateau sous forme d'un couple (i,j)'


    coordonné_pixel((2,2))
    >>> (250,250)
    cordonné
    """
    i, j = sommet  # soit i et j des coordonnées du sommet
    return taille_marge + j * taille_case, taille_marge + i * taille_case


# on additionne la taille de la marge avec j fois la taille de la case

def get_table(fichier):  # soit table est une grille
    "cette fontion permet de recuperer la grille dans le fichier.txt en utilisant la focntion predefiinit  open qui est ennoncer ci dessous "
    ouverture = open(fichier, 'r')
    table = []  # initialisation d'une liste vierge
    for lignes in ouverture:  # on parcours l'enssemble des lignes qu'il y'a dans ouverture
        table.append(
            lignes)  # ainsi on ajoute dans la liste grille deja cree  precedement l'enssemble des lignes parcouru par la boucle for '

    return table


# representation de l'état du jeu


# definition de etat
# etat es vide au debut du jeu il  est modifier au cours du jeu
def tri_seg(sgmt):
    """


    sgmt : TYPE


    Returns

    sgmt : TYPE


    """
    # print(sgmt)  # on affiche le segment
    if sgmt[1] < sgmt[0]:  # si la valeur du deuxieme indice est inf a la valeur du premier
        sgmt = (sgmt[1], sgmt[0])  # sgm[1=x  ,
    return sgmt


def est_trace(etat, sgmt):
    """
    Fonction qui renvoie True si segment est tracé dans etat, False sinon.

    Paramètres type :
    -etat : Dictionnaire-----> dernier expose l'etat de notre dico(etat)
    -segment : Tuple de tuple (couple de sommets)

    Return type : Booléen

    >>> est_trace( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((0,1),(1,1))

    False

    >>> est_trace( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1, } , ((2,3),(2,4))
    True


    """
    sgmt = tri_seg(sgmt)  # a l'aide de la focntion tri-seg
    if sgmt in etat:  # si le segment est bien dans le dico
        return etat[sgmt] == 1  # le segment prend 1 comme valeur
    return False


def est_interdit(etat, sgmt):
    """
    Fonction qui renvoie True si segment est interdit dans etat, False sinon.

    Paramètres type :
    -etat : Dictionnairee-----> dernier expose l'etat de notre dico(etat)
    -segment : couple de couple

    Return type : Bool

    >>> est_interdit( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((2,4),(3,4))

    False


est_interdit( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((2,1),(3,1)

    True
    """

    sgmt = tri_seg(sgmt)  # on fais appele a la focntion predefinit tri_seg
    for cle, valeurs in etat.items():  # on parcours le dico
        if (cle == sgmt) and (valeurs == -1):  # si la clé est egal a segment et ça valeur est egal a -1 on renvois true
            return True
        else:
            return False


def est_viege(etat, sgmt):
    """
    Renvoie True si le segment est vierge dans etat, False sinon.


    Paramètres type :
    -etat : Dictionnaire-----> dernier expose l'etat de notre dico(etat)
    -segment :couple de couple

    Return type : Bool

    >>> est_vierge( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((1,1),(2,1))
    False

    est_vierge( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((8,1),(5,0))
    True
    """

    segment = tri_seg(sgmt)  # on fais appele a la focntion predefinit tri_seg
    return sgmt not in etat  # le segment n'est donc pas dans l'etat (dico)


def tracer_segment(etat, sgmt):
    """
    Modifie le paramètre etat afin de representer le fait que segment est maintenant tracé.

    Paramètres type :
    -etat : Dictionnaire-----> dernier expose l'etat de notre dico(etat)
    -segment : couple de couple



    >>> tracer_segment( {
        ((0, 1), (1, 1)) : 1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) :-1} , ((2,3),(2,4))

    { ((0, 1), (1, 1)) : 1,
      ((1, 1), (2, 1)) : 1,
      ((2, 1), (3, 1)) : -1,
      ((1, 4), (2, 4)) : -1,
      ((2, 4), (2, 5)) : -1,
      ((2, 3), (2, 4)) : 1,
      ((2, 4), (3, 4)) : 1 }

    """
    sgmt = tri_seg(sgmt)  # on fais appele a la focntion predefinit tri_seg
    print(sgmt)  # on affiche segment a a qui on a affecter la focntion tri_seg(sgmt)
    etat[sgmt] = 1  # la valeur du segment est desormais 1


def interdire_segment(etat, sgmt):
    """
    Modifie le paramètre etat afin de representer le fait que segment est maintenant interdit.

    Paramètres type :
    -etat : Dictionnaire-----> dernier expose l'etat de notre dico(etat)
    -segment :couple de couple


    >>> interdire_segment( {

        ((0, 1), (1, 1)) :-1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((1,1),(2,1))

     { ((0, 1), (1, 1)) :-1
       ((1, 1), (2, 1)) : -1,
       ((2, 1), (3, 1)) : -1,
       ((1, 4), (2, 4)) : -1,
       ((2, 4), (2, 5)) : -1,
       ((2, 3), (2, 4)) : 1,
       ((2, 4), (3, 4)) : 1 }

    """
    sgmt = tri_seg(sgmt)  # on fais appele a la focntion predefinit tri_seg
    etat[sgmt] = -1  # valeur de la clé segment est egal a -1


def effacer_segment(etat, sgmt):
    """
    Modifie le parametre etat afin de representer le fait que segment est maintenant vierge.

    Paramètres type :
    -etat : Dictionnaire-----> dernier expose l'etat de notre dico(etat)
    -segment : couple de couple



    >>> effacer_segment( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , ((1,1),(2,1))

   { ((0, 1), (1, 1)) : -1,
     ((2, 1), (3, 1)) : -1,
     ((1, 4), (2, 4)) : -1,
     ((2, 4), (2, 5)) : -1,
     ((2, 3), (2, 4)) : 1
     ((2, 4), (3, 4)) : 1
   }

    """
    sgmt = tri_seg(sgmt)  # on fais appele a la focntion predefinit tri_seg
    print(sgmt)
    etat.pop(sgmt)  # ici on fais appele  a la fonction .pop qui suprime la clé segment du dico


def segments_traces(etat, smt):
    """
    Fonction renvoyant la liste des segments tracés adjacents à sommet dans etat.

    Paramètres type
    -etat: Dictionnaire-----> dernier expose l'etat de notre dico(etat
    -sommet :COUPLE

    Return type : Liste

    >>> segment_traces ( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , (2, 4) )

    [( (2, 4), (2, 5)]

    """
    (i, j) = smt  # on affecte au sommet des coordonnées
    sgmts = []  # on declare une liste vide
    for voisin in [(i, j + 1), (i, j - 1), (i + 1, j), (
    i - 1, j)]:  # si voisin c'est dans la liste qui contient les coordonnées suivantes  (i,j+1),(i,j-1),(i+1,j),(i-1,j)
        sgmt = tri_seg(
            ((i, j), voisin))  # soit sgmt une focntion tri_seg qui prend comme paramettre la coordonnées ((i,j),voisin)
        if sgmt in etat:  # si le sgmt est dans le dico (etat)
            if etat[sgmt] == 1:  # le segment prend comme valeur 1
                sgmts.append(sgmt)  # ainsi on ajoute a la liste deja definit au debut la clé sgmt
    return sgmts  # on renvois sgmt


def segments_interdits(etat, smt):
    """
    Fonction renvoyant la liste des segments interdits adjacents à sommet dans etat.

    Paramètres type:
    -etat: Dictionnaire-----> dernier expose l'etat de notre dico(etat
    -sommet : Tuple (un couple de sommet)

    Return type : Liste

    >>> segments_interdits ( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 } , (0,1))

    [((0, 1), (1, 1))]

    """
    (i, j) = smt  # on affecte au sommet des coordonnées
    sgmts = []  # on declare une liste vide
    for voisin in [(i, j + 1), (i, j - 1), (i + 1, j), (
    i - 1, j)]:  # si voisin c'est dans la liste qui contient les coordonnées suivantes  (i,j+1),(i,j-1),(i+1,j),(i-1,j)
        sgmt = tri_seg(
            ((i, j), voisin))  # soit sgmt une focntion tri_seg qui prend comme paramettre la coordonnées ((i,j),voisin)
        if sgmt in etat:  # si le sgmt est dans le dico (etat)
            if etat[sgmt] == -1:  # on affecte a la clé sgmt la valuer -1
                sgmts.append(sgmt)  # ainsi on ajoute a la liste deja definit au debut la clé sgmt
    return sgmts


def segments_vierges(etat, smt):
    """
    Fonction renvoyant la liste des segments vierges adjacents à sommet dans etat.

    Paramètres type:
    -etat: Dictionnaire-----> dernier expose l'etat de notre dico(etat
    -sommet : couple

    Return type : Liste

    >>> segments_vierges( {
        ((0, 1), (1, 1)) : -1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : -1,
        ((1, 4), (2, 4)) : -1,
        ((2, 4), (2, 5)) : -1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 }, (1,1))

    [((1, 1), (1, 2)), ((1, 0), (1, 1))]

    """
    (i, j) = smt  # on affecte au sommet des coordonnées
    sgmts = []  # on declare une liste vide
    for voisin in [(i, j + 1), (i, j - 1), (i + 1, j), (
    i - 1, j)]:  # si voisin c'est dans la liste qui contient les coordonnées suivantes  (i,j+1),(i,j-1),(i+1,j),(i-1,j)
        sgmt = tri_seg(
            ((i, j), voisin))  # soit sgmt une focntion tri_seg qui prend comme paramettre la coordonnées ((i,j),voisin)
        if sgmt not in etat:  # si le sgmt est dans le dico (etat)
            sgmts.append(sgmt)  # ainsi on ajoute a la liste deja definit au debut la clé sgmt
    return sgmts


def seg_colle(case):
    """


    Parameters
    ----------
    case :tuple


    Returns
    -------
    sgmt :LISTE


    """
    (i, j) = case  # soit case des coordonnées
    smts_1 = [(i, j), (i + 1, j + 1)]  # liste
    smts_2 = [(i + 1, j), (i, j + 1)]  # liste
    sgmt = []  # liste vide
    for smt in smts_1:  # on parcourtous les elements de la liste 1
        for cord in smts_2:  # on parcours les elmt de la liste 2 en parallele
            sgmt.append(tri_seg((smt, cord)))  # on ajoute a la liste vide deja definit -->tri_seg((smt,cord)
    return sgmt


def statut_case(indices, etat, case):
    """
    cette fonction verifie si il est possible d'ajouter des segments


    -indices : LISTE DE LISTE
    -etat: DICO
    -case : COUPLE

    Return type : soit int , ou chaine de caractaire ("positif" , "negatif")

    >>> statut_case(
    [None, None, None,None,None]
    [2,2, None, None, None,None],
    [ 2,1,None , 0, 3],
    [1, None, None , None , 2, 3],
    [2, 2 , 2, 2, 2, None]]),

    _____
    22__3
    21_03
    1__23
    2222_

     {  ((0, 1), (1, 1)) : 1,
        ((1, 1), (2, 1)) : 1,
        ((2, 1), (3, 1)) : 1,
        ((1, 4), (2, 4)) : 1,
        ((2, 4), (2, 5)) : 1,
        ((2, 3), (2, 4)) : 1,
        ((2, 4), (3, 4)) : 1 },

    case=(0,4) )

    0
    """
    (i, j) = case  # soit case des coordonnées
    if indices[i][j] == None:  # si l'indice des coordonnées (i,j) est egal a None
        return None  # on le renvois
    # on declare deux liste vide
    liste_une = []
    liste_deux = []
    for sgmt in seg_colle(
            case):  # on parcours la liste qui est renvoiyer par la focntion seg_colle qu'on a deja predefinit
        if est_trace(etat, sgmt):  # si sgmt est bien tracer
            liste_une.append(sgmt)  # on l'ajoute a la premiere liste
        if est_interdit(etat, sgmt):  # si sgmt est interdit c'est a dire la clé sgmt prend comme valeur -1
            liste_deux.append(sgmt)  # on lajoute anotre deuxieme liste
    # ainsi on aura deux liste
    # une qui conient des segment tracé
    # une qui contient des segment interdit

    if indices[i][j] == len(liste_une):  # si l'indice des coordonnées (i,j) est egale a la longeure de la liste_une
        return 0  # on retourn la valeur  zero 0
    if indices[i][j] > len(liste_une):  # si l'indice des coordonnées (i,j) est superieur a la longeure de la liste_une
        return 'positif'
    if indices[i][j] < len(liste_une) or len(liste_deux) > indice[i][j]:  # si l'indice des coordonnées (i,j) est inferieur a la longeure de la liste_une
        return 'negatif'


##########################################################################################################TACHE 02 ###################################

def satisfaction(indices, etat):
    """
    Renvoie True lorsque chaque indice est satisfait :
    chaque case contenant un nombre k compris entre 0 et 3 a exacetement k cotés tracés.


    Parameters
    ----------
    indices : tuple
    etat : dico


    Returns bool
    -------
    bool
    """
    for k in range(len(indices)):  # on parcours le tuple indice
        for f in range(len(indices[0])):
            # boucle imbriqué
            if statut_case(indices, etat, (k, f)) != 0 and statut_case(indices, etat, (k, f)) is not None:
                # si le return de de la focntion statut_case est différent de zero et de None

                return False  # on renvois False

    return True


def longueur_boucle(etat, sgmt):
    """
    Fonction renvoyant None si segment n'appartient pas à la boucle, sinon elle renvoie
    la longueur de la boucle à laquelle il appartient.

    Paramètres type :
    -etat: Dictionnaire
    -segment: Couple de coordonnées

    Return type : int

    >>> longueur_boucle ({
    ((0,0),(1,0)) : 1,
    ((1,0),(1,1)) : 1,
    ((0,1),(1,1)) : 1,
    ((0,0),(0,1)) : 1,
    },
    ((0,1),(1,1)))

    4

     >>> longueur_boucle ({
    ((0,0),(1,0)) : 1,
    ((1,0),(1,1)) : 1,
    ((0,1),(1,1)) : 1,
    ((0,0),(0,1)) : 1,
    ((1,1),(1,2)) : 1
    },
    ((0,1),(1,1))))

    None

    """
    start = sgmt[0]
    avant = sgmt[0]
    actuel = sgmt[1]
    t = 0
    while actuel != start:
        sgmt = segments_traces(etat, actuel)
        if len(sgmt) != 2:
            return
        else:
            for i in range(len(sgmt)):
                if sgmt[i] != tri_seg((avant, actuel)):
                    if sgmt[i][0] == actuel:
                        avant = actuel
                        actuel = sgmt[i][1]
                        break
                    else:
                        avant = actuel
                        actuel = sgmt[i][0]
                        break
        t += 1
    return t + 1


####################################################################################################TACHE 03 ########################################


def indice(table):
    """
    cette fonction prend comme paramettre une grille==>liste et renvoie la liste des indice

    Parameters
    grille : LISTE
    Returns LISTE
    indices : LISTE


    """
    indices = []  # ON DECLARE une liste vide nomée (indice)
    c = 0
    for ligne in table:  # on parcours lles lignes du tableau
        indices.append([])
        for indice in ligne:
            if indice == '_':  # si l'indice est egale a (tiré)
                indices[c].append(None)
            if indice in ['0', '1', '2', '3']:  # si l'indice apartien a la liste qui contien les chiffre 0.2.1.3
                indices[c].append(
                    int(indice))  # on rajoute a la liste (indice )la l'entier qui represente la valeur de la clé indice
        c += 1

    return indices


def exprimer_indice(etat, indices):
    "fonction affichant les indice en fonction du statut de la case qui porte l'indice "
    for ligne in range(len(indices)):
        for colonne in range(len(indices[ligne])):
            if indices[ligne][colonne] != None:
                x, y = case_vers_pixel((ligne, colonne))
                if statut_case(indices, etat, (ligne, colonne)) == 0:
                    texte(x + taille_case / 3, y + taille_case / 5, f"{indices[ligne][colonne]}", 'blue', taille=25)
                elif statut_case(indices, etat, (ligne, colonne)) == 'negatif':
                    texte(x + taille_case / 3, y + taille_case / 5, f"{indices[ligne][colonne]}", 'red', taille=25)
                else:
                    texte(x + taille_case / 3, y + taille_case / 5, f"{indices[ligne][colonne]}", taille=25)


def smt(indice):
    """


    Parameters
    ----------
    indice :LISTE
    Returns
    -------
    sgmts : LISTE


    """
    sgmts = []
    ligne = len(indice[0])
    # boucle imbriqué
    for i in range(len(indice) + 1):
        for j in range(ligne + 1):
            sgmts.append((i, j))  # on ajoute a la liste les cordonéées (i,j)
    return sgmts


def exprimer_smt(smt):  # cette focntion exprime tous les sommets avec un fond noir
    for i in smt:
        k, f = case_vers_pixel((i[0], i[1]))
        cercle(k, f, 5, remplissage="black")


def exprimer_table(etat):
    efface("segment")
    efface("interdit")
    for key, values in etat.items():
        x0, y0 = case_vers_pixel(key[0])
        x1, y1 = case_vers_pixel(key[1])
        if values == 1:
            ligne(x1, y1, x0, y0, couleur='black', epaisseur=3, tag="segment")
        if values == -1:
            texte((x0 + x1) / 2, (y0 + y1) / 2,
                  "x", couleur="red", ancrage="center", tag="interdit")


def quantite_ST(etat):  # combien de segments qui sont tracés
    r = 0
    for i in etat.values():
        if i == 1:
            r += 1
    return r


def Bouton_menu(Bouton, TEXTE):
    """
    affiche le bouton et le texte
    """
    # print(Bouton[0][0] + 50, Bouton[0][1], Bouton[1][0] - 50, Bouton[1][1] - 25, )
    rectangle(Bouton[0][0] + 50, Bouton[0][1], Bouton[1][0] - 50, Bouton[1][1] - 25, couleur='pink', epaisseur=1,
              tag='game')
    texte(Bouton[0][0] + 20, Bouton[0][1] + 10, TEXTE, couleur='orange', taille=25, tag='game')


def segment_satisfait(segment, indices):
    """
    Fonction qui permet de vérifier si le segment possède des coordonnées
    se situant bien dans les limites de la grille.
    """
    i, j = segment
    if 0 <= i[0] <= len(indices) and 0 <= i[1] <= len(indices[0]):
        if 0 <= j[0] <= len(indices) and 0 <= j[1] <= len(indices[0]):
            return True
    return False


def obtenir_segment(x, y):
    " cette fonction a pour but l'obtention des segment sur la grille du jeux quand on clic "
    dx = (x - taille_marge) / taille_case
    dy = (y - taille_marge) / taille_case
    if -0.2 < dx - round(dx) and dx - round(dx) < 0.2 and (-0.2 > dy - round(dy) or dy - round(dy) > 0.2):
        if segment_satisfait(((int(dy), round(dx)), (int(dy) + 1, round(dx))), indices): # empeche de tracer en segment en dehors de la grille
            return ((int(dy), round(dx)), (int(dy) + 1, round(dx)))
    if -0.2 < dy - round(dy) and dy - round(dy) < 0.2 and (-0.2 > dx - round(dx) or dx - round(dx) > 0.2):
        if segment_satisfait(((round(dy), int(dx)), (round(dy), int(dx) + 1)), indices): # empeche de tracer en segment en dehors de la grille
            return ((round(dy), int(dx)), (round(dy), int(dx) + 1))


def victoire_1(indices, etat):
    """
    Fonction qui renvoie vrai si l'indice de chaque case est satisfait
    """
    if satisfaction(indices, etat):
        return True
    return False


def victoire_2(etat):
    """
    Fonction qui renvoie vrai si les segments forment une boucle unique.
    """
    cmpt_segment = quantite_ST(etat)
    for seg2 in etat:
        if longueur_boucle(etat, seg2) == cmpt_segment:
            return True
    return False


def solveur_depart(indices):
    """
    Fonction qui détermine un bon sommet de départ pour le solveur,
    """
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if indices[i][j] == 3:  # si l'indice vaut 3
                return (i, j)
            elif indices[i][j] == 2:  # si l'indice vaut 2
                return (i, j)
            elif indices[i][j] == 1:  # si l'indice vaut 1
                return (i, j)
    return (0, 0) # pas d'indice 1, 2, 3 dans la grille


def solveur(etat, sommet, indices):
    """
    Fonction qui cherche la solution d'une grille
    :param1: dictionnaire
    :param2: tuple
    :param3: liste de listes
    :return value: booleen
    """
    liste = segments_traces(etat, sommet)
    if len(liste) == 2:
        if satisfaction(indices, etat):
            return True
        else:
            return False
    if len(liste) > 2:
        return False
    if len(liste) == 0 or len(liste) == 1:
        liste2 = segments_vierges(etat, sommet)
        for segment in liste2:
            if segment_satisfait(segment, indices):
                exprimer_table(etat)
                tracer_segment(etat, segment)
                mise_a_jour()
                if sommet == segment[0]:
                    sommet2 = segment[1]
                else:
                    sommet2 = segment[0]
                V = solveur(etat, sommet2, indices)
                if V:
                    return True
                else:
                    effacer_segment(etat, segment)
                    segment_satisfait(segment, indices)
                    mise_a_jour()
        return False


if __name__ == "__main__":
    # on commence d'abors par l'affectation initial
    cree_fenetre(500, 500)
    taille_case = 80
    taille_marge = 80
    etat = {}  # initialisation de notre dicionnaire

    grille = random.choice(["grille1.txt", "grille2.txt", "grille-triviale.txt", "grille3.txt", "grille4.txt"])
    grille1 = False
    grille2 = False
    grille3 = False
    grille4 = False
    grille5 = False
    # liste des coordonnées des bouton du menu
    Bouton = [[(115, 130), (485, 210)], [(115, 230), (485, 310)], [(115, 330), (485, 410)], [(115, 430), (485, 510)],
              [(115, 530), (485, 610)], [(115, 630), (485, 710)]]
    Bouton_menu(Bouton[0], '          grille aléatoire')
    Bouton_menu(Bouton[1], '          1ere grille ')
    Bouton_menu(Bouton[2], '          2eme grille ')
    Bouton_menu(Bouton[3], '          3eme grille')
    Bouton_menu(Bouton[4], '          4eme grille')
    Bouton_menu(Bouton[5], '          5eme grille')

    while True:  # tant que le joueur n'a pas cliquer
        clique = attend_clic_gauche()
        # repérer les clic
        if Bouton[0][0][0] <= clique[0] and clique[0] <= Bouton[0][1][0] and \
                Bouton[0][0][1] <= clique[1] and clique[1] <= Bouton[0][1][1]:
            break
        if Bouton[1][0][0] <= clique[0] and clique[0] <= Bouton[1][1][0] and \
                Bouton[1][0][1] <= clique[1] and clique[1] <= Bouton[1][1][1]:
            grille1 = True
            break
        elif Bouton[2][0][0] <= clique[0] and clique[0] <= Bouton[2][1][0] and \
                Bouton[2][0][1] <= clique[1] and clique[1] <= Bouton[2][1][1]:
            grille2 = True
            break
        elif Bouton[3][0][0] <= clique[0] and clique[0] <= Bouton[3][1][0] and \
                Bouton[3][0][1] <= clique[1] and clique[1] <= Bouton[3][1][1]:
            grille3 = True
            break
        elif Bouton[4][0][0] <= clique[0] and clique[0] <= Bouton[4][1][0] and \
                Bouton[4][0][1] <= clique[1] and clique[1] <= Bouton[4][1][1]:
            grille4 = True
            break
        elif Bouton[5][0][0] <= clique[0] and clique[0] <= Bouton[5][1][0] and \
                Bouton[5][0][1] <= clique[1] and clique[1] <= Bouton[5][1][1]:
            grille5 = True
            break
    if grille1:
        grille = "grille-triviale.txt"
    if grille2:
        grille = "grille1.txt"
    if grille3:
        grille = "grille2.txt"
    if grille4:
        grille = "grille3.txt"
    if grille5:
        grille = "grille4.txt"
    indices = indice(get_table(grille))
    efface_tout()
    while True:
        efface_tout()
        ev = donne_ev()
        tev = type_ev(ev)
        exprimer_indice(etat, indices)
        exprimer_smt(smt(indices))
        rectangle(taille_marge - 10, taille_marge - 10, (taille_marge + taille_case * len(indices[0])) + 10,
                  (taille_marge + taille_case * len(indices)) + 10)
        exprimer_table(etat)
        qtt = quantite_ST(etat)

        if tev == "ClicDroit":
            x = abscisse(ev)
            y = ordonnee(ev)
            # sgmt = quantite_ST(x, y)
            sgmt = obtenir_segment(x, y)
            if sgmt is not None:
                if sgmt not in etat:  # si le segment n'est pas interdit on le trace sinon on l'efface
                    interdire_segment(etat, sgmt)
                else:
                    effacer_segment(etat, sgmt)

        if tev == "ClicGauche":
            x = abscisse(ev)
            y = ordonnee(ev)
            sgmt = obtenir_segment(x, y)
            if sgmt is not None:
                if sgmt not in etat:  # si le segment n'est pas tracé on le trace sinon on l'efface
                    tracer_segment(etat, sgmt)
                else:
                    effacer_segment(etat, sgmt)
                # On affiche dans la console le statut de nos deux conditions de victoires à chaque clic gauche
                print("Indices tous satisfait :", str(victoire_1(indices, etat)))
                print("Segments formants une boucle unique :", str(victoire_2(etat)))

        if tev == 'Quitte':  # on sort de la boucle si on clique sur la croix de la fenetre
            break

        if victoire_1(indices, etat) and victoire_2(etat):  # Si nos deux conditions de victoire sont réunis
            texte(300, 10, "Victoire")

        if tev == "Touche":  # Si l'évènement est une touche du clavier
            if touche(ev) == "s":  # si la touche vaut "s"
                sommet = solveur_depart(indices)  # on cherche un sommet adéquate pour le solveur
                solveur(etat, sommet, indices)  # on lance le solveur

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()

    ferme_fenetre()
