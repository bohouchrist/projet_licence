# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:04:54 2021

@author: bohou
"""


from fltk import *
from random import *
##Tâche 1: Structures de données##

##Chargement de la grille##

def recupere_indices_grille(fichier_text):
    """permet de recuperer les donner d'un fichier texte (grille(n).txt)
       et de creer la liste des indices de la grille """
    grille = open(fichier_text)
    liste_indices_grille= []
    for ligne in grille:
        liste_indices_grille.append(ligne)
    return liste_indices_grille



def cst_indices(liste_indices_grille):
    """ permet de créer la liste de listes indices à paritis de 
    la liste des indices de la  grille"""
    indices=[]
 #   print(liste_indices_grille)
    
    
    for i in range(len(liste_indices_grille)-1) :
        if  len(liste_indices_grille[i]) != len(liste_indices_grille[i+1]):
            print('presence de lignes de longueurs différentes dans la grille')
    i=0
    for ligne in liste_indices_grille :
        indices.append([])


        
        for indice in ligne[:-1]:
            if indice == '_':
                indices[i].append(None)
            if indice in ['0','1','2','3']:
                indices[i].append(int(indice))
            if indice != '_' and indice not in ['0','1','2','3'] :
                print('présence d’un caractère interdit dans la grille')
        i+=1
    return indices 








"""travail de manipulation des segments et de l’état de la grille"""

###Fonctions d’accès##

def est_trace(etat,segment):
      if etat[segment]== 1:

        return True
      else:
          return  False



def est_interdit(etat,segment):
        if etat[segment]==-1:
            return True
        else:
            return False


def est_vierge(etat, segment):
    if segment not in etat:
        return True
    else :
        return False


def tracer_segment(etat, segment):
    etat[segment]=1

def interdire_segment(etat, segment):
    etat[segment]=-1

def effacer_segment(etat, segment):
    etat.pop(segment)

def segments_traces(etat, sommet):

    liste_segment_traces=[]
    for segment in etat : 
        if est_trace(etat,segment)== True:
            if sommet in segment:
                liste_segment_traces.append(segment)
    return liste_segment_traces

def segments_interdits(etat, sommet):
    liste_segments_interdits=[]
    for segment in etat :
          if est_interdit(etat,segment)== True:
            if sommet in segment :
                liste_segments_interdits.append(segment)
    return liste_segments_interdits


def segments_vierges(etat, sommet):
    liste_segment_vierges=[]
    if est_vierge(etat,segment)== True:
            if sommet in segment :
                liste_segment_vierges.append(segment)
    return liste_segment_vierges






def statut_case(indices, etat, case):
    " fonction qui verifie le statut de la case "
    (i, j)= case
    
    if i<m and j<n:
        segments_adjacents= [((i,j),(i+1,j)),((i,j),(i,j+1)),
                     ((i,j+1),(i+1,j+1)),((i+1,j),(i+1,j+1))]
        
        
        if indices[i][j] == None :
            return None
        else:
            segments_adjacents_trace=[]
            segments_adjacents_interdit=[]
            for segment in segments_adjacents :
                if segment in etat:
                    
                    if est_trace(etat,segment):
                        segments_adjacents_trace.append(segment)
                        if est_interdit(etat,segment):
                            segments_adjacents_interdit.append(segment)
           


        if indices[i][j]== len(segments_adjacents_trace):
            return 0
        if indices[i][j] > len(segments_adjacents_trace):
            return 'positif'
        if indices[i][j] < len(segments_adjacents_trace) or 4-indices[i][j] < len(segments_adjacents_interdit): 
            return 'negatif '

def ordonner(segment):
    """ d’ordonner correctement les segments passés en paramètre (avec le plus petit sommet
     en premier) avant de lire ou d’écrire dans le dictionnaire etat."""
    
    if segment[1] < segment[0]:
        segment =  ((segment[1],segment[0]))
    return segment 
 
####Tâche 2 : conditions de victoire####


""" maintien dans une variable globale du programme le nombre total 
 de segments tracés"""


def cases_satisfaites(indices,etat):
    """Verifie si chaque indice est satisfait : chaque case 
    contenant un nombre k compris entre 0 et 3 a exactement k côtés
    tracés. Si oui elle renvoie True sinon False """
    
    
    lst1=[]
    lst2=[]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            case = (i,j)
            if indices[i][j] in [0,1,2,3]:

                lst1.append(case)
                if statut_case(indices, etat, case) == 0:
                    lst2.append(case)
    if len(lst1)== len(lst2):
        
        return True
       
    return False


        
def longueur_boucle(etat, segment):
    segment = ordonner(segment)
    depart = segment[0]
    precedent = segment[0]
    courant = segment[1]
    longueur= 1
    while courant != depart :
        lst= segments_traces(etat, courant)
        lst1=segments_traces(etat, depart)

    
        if len(lst)!=2:
            return  None
        if len(lst1)!= 2:
            return None
        else:
             for i in range(len(lst)):
                 if lst[i] != ordonner((precedent,courant)):
                      if lst[i][0]==courant:
                            precedent = courant
                            courant= lst[i][1]
                            break
                      else:
                            precedent = courant
                            courant = lst[i][0]
                            break
        
        longueur +=1
        
    return longueur 




def lst_segment_tracer(etat):
    lst= []
    for segment in etat :
        if etat[segment] == 1 :
            lst.append(segment)
        
    return lst


def conditions_victoires(etat,indices,nombre,l):
   # print(longueur_boucle(etat, l_seg_tracées[0]))
   # print(nombre)
    
        
    if nombre  == longueur_boucle(etat, l[0]) and cases_satisfaites(indices,etat):
        return True
        
    
            
             
                 
            


 

    
  


##Tâche 3: Interface graphique###


"dans un premier temps afficher la grille"







        
               
def coordonnées(sommet):
    """convertir les cordonnées d'un sommet en pixel """
    (i,j)= sommet 
    (si,sj)=(taille_marge + j * taille_case, taille_marge + i * taille_case)
    return (si,sj)

def tracer(segment):
    """permet de tacer le segment dans la grille"""
    
    ((ai,aj),(bi,bj))= segment 
    (ax,ay)=coordonnées((ai,aj))
    (bx,by)= coordonnées((bi,bj))
    (ligne(ax,ay,bx,by, couleur="black", epaisseur=4))

def interdit(segment):
    #la croix
   ((ai,aj),(bi,bj))= segment 
   (ax,ay)=coordonnées((ai,aj))
   (bx,by)= coordonnées((bi,bj))
   ligne((ax+bx)/2-4,(ay+by)/2-4,(ax+bx)/2+4,(ay+by)/2+4, couleur="red", epaisseur=2)
   ligne((ax+bx)/2+4,(ay+by)/2-4,(ax+bx)/2-4,(ay+by)/2+4,couleur="red", epaisseur=2)
   
    
    
    

def dessine(indices,etat) :
    for i in range(m+1):
        for j in range(n+1):
            cercle(150+ j*50, 150+ i*50, 3, remplissage="black")
            
   


    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if indices[i][j] in [0,1,2,3]:
                indice= indices[i][j]
                case = (i,j)
                u = (325+100*j)/2
                v = (315+100*i)/2
                if statut_case(indices, etat, case) == 0:
                    couleur_indice= "blue"
                    texte(u, v , str(indice), couleur= couleur_indice)
                elif statut_case(indices, etat, case) == 'positif':
                    couleur_indice= "black"
                    texte(u, v , str(indice), couleur= couleur_indice)
                else :
                
                    couleur_indice= "red"
                    texte(u, v , str(indice), couleur= couleur_indice)
              
          

def mise_en_forme(etat): 
    """permet de tracer ou interdit les segment de etat """
    for segment in etat :
        if etat[segment] == 1:
            tracer(segment)
            
        if etat[segment] == -1:
            interdit(segment)

def clic_vers_segment(x,y):
    """permet de decterter si le joueur a cliquer sur un segment """
    dx = (x - 150) /taille_case
    dy = (y -150)  /taille_case 
    if 150-10<x and x< 150+50*m+10 and 150-10<y and y<150+50*n+10:
        
        if -0.2 < dx- round(dx) and dx-round(dx)< 0.2  and (-0.2 > dy- round(dy) or dy-round(dy)> 0.2):
            return ((int(dy),round(dx)),(int(dy)+1,round(dx)))
        if -0.2 < dy- round(dy) and dy-round(dy)< 0.2 and (-0.2 > dx- round(dx) or dx-round(dx)> 0.2):
            return ((round(dy),int(dx)),(round(dy),int(dx)+1))


            

    
def créer_menu(zone,contenu):
    """
        Fonction qui créer et fait apparaitre un rectangle en entrant les
        coordonnées des quatres coins du rectangle et permet placer un texte
        dans le rectangle sur une fenetre
    """

    rectangle( zone[0][0] , zone[0][1] , zone[1][0], zone[1][1],couleur='black' , epaisseur=2, )
    texte(zone[0][0] + 10, zone[0][1] + 10, contenu, couleur='black',taille=20)  



def lst_segments(m,n):
    
    """ 
    renvoie la liste de tous les segmnts d'une grille 
    
    >>>lst_segments(2,2) (grille triviale)
    [((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((1, 0),
   (2, 0)), ((1, 1), (2, 1)), ((1, 2), (2, 2)), ((0, 0), (0, 1)), 
   ((0, 1), (0, 2)), ((1, 0), (1, 1)), ((1, 1), (1, 2)), ((2, 0), (2, 1)),
   ((2, 1), (2, 2))]
    
    """
    lst_segment =[]
    for i in range(m):
        for j in range(n+1):
            seg_v= ((i,j),(i+1,j))
            lst_segment.append(seg_v)
    for i in range(m+1):
        for j in range(n):
          seg_h =((i,j),(i,j+1)) 
          lst_segment.append(seg_h)

    return lst_segment


def seg_adj_case(case):
    
    (i,j)= case
    lst= [((i,j),(i+1,j)),((i,j+1),(i+1,j+1)),((i,j),(i,j+1)), ((i+1,j),(i+1,j+1))]
    return lst 

#print(seg_adj_case((1,1)))
def seg_adj_case_etat1(case):
    lst =[]
    for segment in seg_adj_case(case):
        if segment in etat1:
            lst.append(segment)
    return lst

def case_adj(segment):
    """
    renvoie la liste des cases adjacentes au segment "
    >>>case_adj(((0, 6), (1, 6)) grille1
    [(0, 5)]
    """
                
    lst =[]    
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            case =(i,j)
            if segment in [((i,j),(i+1,j)),((i,j+1),(i+1,j+1)),((i,j),(i,j+1)), ((i+1,j),(i+1,j+1))]:
                lst.append(case)
    return lst 


def seg_adj_sommet(sommet):
    """ 
    renvoie la liste des segment adjacents au sommet
    >>>seg_adj((1,6))
    [((0, 6), (1, 6)), ((1, 6), (2, 6)), ((1, 5), (1, 6))]
    """
    lst =[]
    for segment in lst_segments(m,n) :
        if sommet in segment :
            lst.append(segment)
    return lst 
            

              
def seg_adj_dans_etat1(etat1,sommet):
    
     """renvoie la liste des segment adjacents à sommet dans l'ensemble"""
     
     lst_seg_adjacent= []
     for segment in  etat1:
        if sommet in segment:
            lst_seg_adjacent.append(segment)
     return   lst_seg_adjacent


def seg_à_tracer(segment,etat1):
    " permet au solveur de verifier "
    
    segment= ordonner(segment)

    for case in case_adj(segment):
        (i,j)= case
        if indices[i][j] == None:
            continue
        if indices[i][j] in [0,1,2,3]:
            if indices[i][j] == 0:
            
                return False
              
                
            if indices[i][j] - len(seg_adj_case_etat1(case)) <1:
                 
            
                return False
   
    return True  




      

def aucune_s(sommet):
     """ permet de verifier que la solution ne passe pas par le sommet 
       autrement ditil existe aucun segment adjaçent au segment dans etat1 
       qui designe l'etat du solveur """
     for segment in seg_adj_sommet(sommet):
         if segment not in etat1 :
             return True
         return False
     



def r_solutions(sommet,etat1,indices):
    """ Fonction qui permet de trouver la solution de la grille et la stocké dans
        etat1 selon l'agorithme du solveur naïve """
    
    lst1 =seg_adj_dans_etat1(etat1,sommet)
    n = len(lst1)
    if n == 2 :
        if cases_satisfaites(indices,etat1):
            return True
        else :
            return False 
        
    if n > 2 :
        return False 
    if  n == 0 or n == 1 :
        lst = list(set(seg_adj_sommet(sommet)) - set(lst1))
        for segment in lst  :
            if seg_à_tracer(segment,etat1):
                if segment not in etat1:
                    tracer_segment(etat1, segment)
                
    
                    som_suiv = segment[1]
                    if som_suiv == sommet :
                       som_suiv = segment[0]
                    resultat = r_solutions(som_suiv,etat1,indices)
                    if resultat:
                        return True
                    else:
                         effacer_segment(etat1, segment)
                        
                    
    if aucune_s(sommet):
        return False
  

 

if __name__ == "__main__":
    #initialisation
    " création du menu d'acceuil "
    etat={}
    etat1 = {}
    taille_marge= 150
    taille_case= 50
    cree_fenetre(600,600)
    image(300,300,"acceuil.jpg")
    zone =(((30,50),(180,100)),((230,50),(380,100)),((430,50),(580,100))\
           ,((200,200),(500,250)),((200,300),(500,350)))
    grille1 = "grille1.txt"
    grille2 = "grille2.txt"
    grille3 = "grille-triviale.txt"
    grille4 =  choice(["grille4.txt","grille5.txt","grille5_2.txt"])
    grille5 = "grille-vide.txt"
    créer_menu(zone[0], '   grille1')
    créer_menu(zone[1], '   grille2')
    créer_menu(zone[2], '   grille3')
    créer_menu(zone[4],  '         grille vide ')
    créer_menu(zone[3], '     autres grilles')
    victoire_joueur = False
    solveur = False  
    solveur_victoire = False
    

    
def dectect_clic_vers_bouton(x,y):
    """ permet de decter le choix de la grille du joueur a partie de la zone
       où il clique"""
       
    if zone[0][0][0] < x < zone[0][1][0] and \
       zone[0][0][1] < y <  zone[0][1][1]: 
            return grille1 
           
              
    elif zone[1][0][0] < x < zone[1][1][0] and \
         zone[1][0][1] < y < zone[1][1][1]:
            
             return grille2
             
    elif zone[2][0][0] < x < zone[2][1][0] and \
         zone[2][0][1] < y < zone[2][1][1]:
             return grille3
    elif zone[3][0][0] < x < zone[3][1][0] and \
         zone[3][0][1] < y < zone[3][1][1]:
             return grille4
    elif zone[4][0][0] < x < zone[4][1][0] and \
         zone[4][0][1] < y < zone[4][1][1]:
             return grille5
         
   
             

while True: # TANT QUE UN BOUTON A PAS ETE PRESSE 
     (x,y) = attend_clic_gauche()
     " le programme attend que le joueur selectionne l'une des  grilles"
     "proposer par l'acceuil"
     grille = dectect_clic_vers_bouton(x,y)
     if grille in [grille1,  grille2 , grille3 , grille4, grille5]:
         break 
        
indices= cst_indices(recupere_indices_grille(grille))

nombres_lignes= len(indices)
nombres_colonnes= len(indices[0])

m= nombres_lignes
n= nombres_colonnes 






efface_tout()
"une fois la grille selectionner on efface tout les dessins pour ensuite afficher"
"la grille selectionner  "

while True:
    efface_tout()
    ev = donne_ev()
    tev = type_ev(ev)
    créer_menu(((5,5),(140,50)), 'solveur')
    créer_menu(((170,5),(370,50)),'recommencer')
    créer_menu(((410,5),(570,50)), 'new grille')
    l_seg_tracées = lst_segment_tracer(etat)
    nombre = len( l_seg_tracées)
    l_seg_tracées1 = lst_segment_tracer(etat1)
    nombre1 = len( l_seg_tracées1)
    dessine(indices,etat)
    mise_en_forme(etat)
    rectangle(150-10, 150-10, 150+50*m+10 ,150+50*n+10)
        
  
    if nombre>0:
        victoire_joueur = conditions_victoires(etat, indices, nombre, l_seg_tracées)
    
    if victoire_joueur:
        texte(200,100, "VICTOIRE !", couleur="green", taille=20)
                
        
    if solveur :
            r_solutions((0,0), etat1, indices)
            dessine(indices,etat1)
            mise_en_forme(etat1)
            if nombre1>0 :
                solveur_victoire = conditions_victoires(etat1, indices, nombre1,l_seg_tracées1 )
                
                
    if  solveur_victoire :
#       si la solution est trouver on arrête de chercher
        texte(130,100, "Grille résolue!", couleur="orange", taille=20)
        solveur = False
        dessine(indices,etat1)
        mise_en_forme(etat1)

    if tev == 'Touche':
        nom_touche = touche(ev)
        if nom_touche == 's':
#       la touche s permet d'appeler le solveur 
            victoire_joueur == False
            solveur = True
            etat= {}
           
    if tev == "ClicGauche":
#        print("Clic gauche  au point", (abscisse(ev), ordonnee(ev)))
        x= abscisse(ev)
        y= ordonnee(ev)
        segment = clic_vers_segment(x,y)
        if segment:
                if segment not in etat:
                    segment = ordonner(segment)
                    tracer_segment(etat,segment)
            
            
                else:
                    segment = ordonner(segment)
                    effacer_segment(etat, segment)
                
        if 5 < x < 140 and 5 < y < 50:
            
             victoire_joueur = False
             solveur = True
             etat= {}
        if 170 < x and x < 370 and 5 < y and y < 50:
            etat= {}
            victoire_joueur = False
            solveur = False
            solveur_victoire = False
            etat1 = {}
        if 410 < x < 570 and 5 < y < 50:
            etat = {}
            solveur = False
            victoire_joueur = False
            solveur_victoire = False
            etat1 = {}
            indices = cst_indices(recupere_indices_grille(choice(["grille4.txt"\
            ,"grille5.txt","grille5_2.txt","grille1.txt","grille2.txt",\
            "grille-triviale.txt","grille-vide.txt"])))
              
         
                
            nombres_lignes= len(indices)
            nombres_colonnes= len(indices[0])
                      
            m= nombres_lignes
            n= nombres_colonnes   
            dessine(indices,etat)
            mise_en_forme(etat)
            rectangle(150-10, 150-10, 150+50*m+10 ,150+50*n+10)
        

    if tev == "ClicDroit" :
        
#       print("Clic droit  au point", (abscisse(ev), ordonnee(ev)))
        x= abscisse(ev)
        y= ordonnee(ev)
        segment = clic_vers_segment(x,y)
        if segment:
            
            if segment not in etat :
                segment= ordonner(segment)
                interdire_segment(etat, segment)
            else:
                segment = ordonner(segment)
                effacer_segment(etat,segment)
    
           
     
  
                
    elif tev == 'Quitte':  # on sort de la boucle
        break

    else:  # dans les autres cas, on ne fait rien
        pass
    
    
            
    mise_a_jour()



ferme_fenetre() 

