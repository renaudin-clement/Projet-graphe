import json
import networkx as nx
import itertools
import matplotlib.pyplot as plt



def json_vers_nx(chemin):
    """fonction permettant de convertir un jeu de données représentant les collaborations 
       en un graphe Networkx exploitable

    Args:
        chemin (String): nom d'un fichier de jeu de donnée au format txt
    Return :
        un graphe G
    """ 
    G = nx.Graph()
    with open(chemin,'r') as fichier:  # ouverture du fichier
        for ligne in fichier:
            data_ligne=[]
            film = json.loads(ligne)  # récupération de la ligne au format json
            # filtre du code
            for nom in film["cast"]:
                acteur = nom.replace("[","").replace("]","") 
                data_ligne.append(acteur)
                G.add_node(acteur)
            G.add_edges_from(list(itertools.combinations((data_ligne),2)))  # combinations('ABCD', 2) = AB AC AD BC BD CD, donc on l'utilise pour les arêtes
    return G

#assert json_vers_nx("data_100.txt")

# Q2

def collaborateurs_communs(G,u,v):
    """ renvoie, pour deux acteurs/actrices donné.e.s, l’ensemble des acteurs/actrices qui ont collaboré.e.s avec ces deux personnes

    Args:
        G : un graphe
        u (String): nom du premier acteur
        v (String): nom du deuxième acteur

    Returns:
        set : ensemble d'acteurs
    """    
    tournee_avec_acteur = set()
    ensemble_acteurA = G[u]                          
    ensemble_acteurB = G[v]          
    for acteur in ensemble_acteurB:
        if acteur in ensemble_acteurA:              
            tournee_avec_acteur.add(acteur)       
    return tournee_avec_acteur

#print(collaborateurs_communs(json_vers_nx("data_100.txt"),"Al Pacino","Lukas Haas"))


# Q3 (code donné)

def collaborateurs_proches(G,u,k):
    """
    Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. 
    La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

#collaborateurs_proches( json_vers_nx("jeux de données réduits-20240521/data_10000.txt"),"Vincent Gallo",10)

def est_proche(G,u,v,k=1):
    """détermine si un acteur u se trouve à distance k d’un autre acteur v

    Args:
        G : un graphe
        u (String): le nom du premier acteur
        v (String): le nom du deuxième acteur
        k (int, optional): la distance (1 par défault)

    Returns:
        bool : vrai si les acteurs sont à distance k, faux si non
    """
    ensemble_proche = collaborateurs_proches(G,u,k)
    if v in ensemble_proche:
        return True
    return False


def distance(G,u,v):
    """Fonction renvoyant la distance entre l'acteur u et l'acteur v. La fonction renvoie None si u ou v est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le premier acteur
        k: le deuxieme acteur
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    if v not in G.nodes:
        print(v,"est un illustre inconnu")
        return None
    distance = 0
    collaborateurs = set()
    collaborateurs.add(u)
    while v not in collaborateurs:
        distance += 1
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return distance


def distance_naive(G,u,v):
    """Fonction optimisée renvoyant la distance entre l'acteur u et l'acteur v.
      La fonction renvoie None si u ou v est absent du graphe.
    
    Args:
        G (nx.Graph): le graphe
        u (String): le premier acteur
        v (String): le deuxieme acteur
    Returns:
        (int) : la distance entre les deux acteurs, ou None
    """
    on= True
    k=0
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    if v not in G.nodes:
        print(v,"est un illustre inconnu")
        return None
    
    if (est_proche(G,u,v,1) == True):
        return 1
    
    while (on==True):
        k += 1
        if (est_proche(G,u,v,k) == True):
            on=False
    return k

#print(distance_naive(json_vers_nx("data_10000.txt"),"Al Pacino","Olivia Newton-John"))

        
# Q4
def centralite(G,u):
    """détermine la plus grande distance entre l'acteur u et les autres acteurs du graphe

    Args:
        G (nx.Graph): un graphe
        u (String): un acteur

    Returns:
        int : la distance 
    """
    collaborateurs = set()
    collaborateurs.add(u)
    distance = 0
    while len(collaborateurs) < len(G):
        distance += 1
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return distance 

  


def centre_hollywood(G):
    """détermine l'acteur le plus central du graphe

    Args:
        G (nx.Graph): un graphe

    Returns:
        String : l'acteur le plus central
    """
    centre = None
    for acteur in G.nodes:
        if centre is None or centralite(G,acteur) < centralite(G,centre):
            centre = acteur
    return centre


# Q5

def eloignement_max(G:nx.Graph):
    """renvoie la distance maximum entre toutes les paires d'acteurs dans G

    Args:
        G (nx.Graph): un graphe

    Returns:
        int : la distance maximum
    """
    distance_max = None
    acteur_max = None
    for acteur in G.nodes:
        if distance_max is None or centralite(G,acteur) > centralite(G,acteur_max):
            acteur_max = acteur
            distance_max = centralite(G,acteur)
    return distance_max



def centralite_groupe(G,S):
    """détermine le centre d'un groupe d'acteur

    Returns:
        String : l'acteur centre
    """    
    centre = None
    for acteur in G.nodes:
        if centre is None or centralite(S,acteur) < centralite(S,centre):
            centre = acteur
    return centre

# autre fonction


def recuperer_data(chemin):
    """renvoie tout les acteurs d'un fichier 

    Args:
        chemin (String): le nom d'un fichier json

    Returns:
        list : une liste d'acteurs
    """
    data=[]
    dataligne=[]
    with open(chemin,'r') as f:
        for line in f:
            dataligne=[]
            film = json.loads(line)
            # filtre du code
            for caster in film["cast"]:
                actors = caster.replace("[","").replace("]","") 
                dataligne.append(actors)
            data.append(dataligne)
    return data
    

def bande_acteur(data):
    """recupere tout les acteurs

    Args:
        data (liste): liste de film contenentdes acteur 

    Returns:
        (liste): liste str d'acteur par film
    """    
    ensemble=set()
    for film in data:
        for acteur in film:
            ensemble.add(acteur)

    return ensemble
    

def arete_existe(G,x,y):
    """ indique si une arrête existe dans le graphe G

    Args:
        G (nx.Graph): un graphe
        x (String): un sommet 
        y (String): un deuxième sommet

    Returns:
        bool: True si l'arrête existe, False si non
    """
    if x.edges in (x,y):
        return True
    else:
        return False
    
    



