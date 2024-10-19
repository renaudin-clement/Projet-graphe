import tkinter

import customtkinter
import itertools
import requetes
import networkx as nx
import matplotlib.pyplot as plt

G = requetes.json_vers_nx("jeux de données réduits-20240521/data_100.txt")
D =requetes.recuperer_data("jeux de données réduits-20240521/data_100.txt")
E=requetes.bande_acteur(D)



def sousgraphe_PAR_FILM(data,x):
    """elle affiche chaque sous graphe des films avec leur acteur

    Args:
        data (list): liste d'acteur par film
        x (int): option reccuperer pour laffichage

    Returns:
        boolean true qui annonce la reactivation du boutton 
    """    
    liste_sousgraphe=[]
    dataligne=[]    
    for film in data:
        dataligne=[]
        sousgraph = nx.Graph()
        for acteur in film:
            dataligne.append(acteur)
            sousgraph.add_node(acteur)
        sousgraph.add_edges_from(list(itertools.combinations((dataligne),2)))
        liste_sousgraphe.append(sousgraph)
    for sousg in liste_sousgraphe: 
        montrer_graph(sousg,x)
    return True
            
        

def montrer_graph(G,x):
    """affiche le graph

    Args:
        G (graph): le graphe complet
        x (int): option reccuperer pour changer l'affichage

    """    
    ax = plt.figure(clear=True)
    optionchoisie(G,x)
    
    print(G)
    return None
    
def afficher_et_sauvegarder(G,x):
    """affiche le graph et le sauvegarde dans le repertoir img

    Args:
        G (graph): le graphe complet
        x (int): option reccuperer pour changer l'affichage
    """        
    fig = plt.figure(clear=True)
    optionchoisie(G,x)
    fig.savefig("img/image.png")



def optionchoisie(G,x):
    """affiche le graph avec l'affichage selectioner 
    
    ne fonctionne pas avec le boutton sous graph par film 
    du a une obligation de le bloquer jusqua la fin du programme

    Args:
        G (graph): le graphe complet
        x (int): l'option qui permet d'avoir un affichage different

    Returns:
        le graph en image
    """    
    if x == 0:
        nx.draw(G,with_labels=True)
        plt.axis("off")
        return plt.show()
    
    if x ==1 :
        options = {
        "font_size": 36,
        "node_size": 50,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 1,
        }
        
        nx.draw(G,with_labels=True, **options)
        plt.axis("off")
        return plt.show()
        
    elif x == 2:
        options = {
        "font_size": 10,
        "node_size": 20,
        "node_color": "red",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 1,
        }
        
        nx.draw_circular(G,with_labels=True, **options)
        return plt.show()
        
    elif x == 3:
        options = {
        "font_size": 10,
        "node_size": 30,
        "node_color": "red",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 1,
        }
        nx.draw_kamada_kawai(G,with_labels=True, **options)
        return plt.show()
        
    elif x ==4:
        options = {
        "font_size": 36,
        "node_size": 50,
        "node_color": "red",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 1,
        }
        
        nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
        H = nx.read_edgelist(path="grid.edgelist", delimiter=":")
        pos = nx.spring_layout(H, seed=200)
        nx.draw(H, pos)
        nx.draw(G,pos,with_labels=False ,**options)
        return plt.show()



