import tkinter
import customtkinter


import networkx as nx
import matplotlib.pyplot as plt
import requetes
import sous_fonction
import oracle




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



        
#__________________________classe des popup _____________________________________________________________________   
#___________________________________________________________________________________________________________________________   
#Popup de la centralite
class Popupcentralite(customtkinter.CTk):
    def __init__(self,distance_centralite):
        super().__init__()
        
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configure window
        self.title("la distance centralite")
        self.geometry(f"{300}x{300}")
        self.textboxEnsemble = customtkinter.CTkTextbox(self, width=250)
        self.textboxEnsemble.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        if distance_centralite == 0:
            self.textboxEnsemble.insert("0.0","est-il le centre ?")
        else:
            self.textboxEnsemble.insert("0.0","la distance centralite de l'acteur A  \n est de "+str(distance_centralite)+"\n")
        self.textboxEnsemble.configure(state="disabled")



# popup distance
class distancePOUPUP(customtkinter.CTk):
    def __init__(self,distance_resultat):
        super().__init__()
        
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configure window
        self.title("la distance parcouru")
        self.geometry(f"{300}x{300}")
        self.textboxEnsemble = customtkinter.CTkTextbox(self, width=250)
        self.textboxEnsemble.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        if distance_resultat == None:
            self.textboxEnsemble.insert("0.0","la distance n'a pas été trouvée")
        else:
            self.textboxEnsemble.insert("0.0","la distance entre l'acteur A a l'acteur B \n est de "+str(distance_resultat)+"\n")
        self.textboxEnsemble.configure(state="disabled")


# popup de la liste des acteurs dans le graphe
class Popup(customtkinter.CTk):
    def __init__(self,E):
        super().__init__()
        
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configure window
        self.title("acteurs présents")
        self.geometry(f"{300}x{300}")
        self.textboxEnsemble = customtkinter.CTkTextbox(self, width=250)
        self.textboxEnsemble.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        for acteur in E:
            print(acteur)
            self.textboxEnsemble.insert("0.0","\""+str(acteur)+"\""+"\n")
        self.textboxEnsemble.insert("0.0","liste des acteurs dans le graphe"+"\n")
        self.textboxEnsemble.configure(state="disabled")
    
    # popup 
class Popupestproche(customtkinter.CTk):
    def __init__(self,ensemble_proche):
        super().__init__()
        
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configure window
        self.title("les acteurs à x distance")
        self.geometry(f"{300}x{300}")
        self.textboxEnsemble = customtkinter.CTkTextbox(self, width=250)
        self.textboxEnsemble.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        print(ensemble_proche)
        if ensemble_proche == None:
            self.textboxEnsemble.insert("0.0","la liste est vide, le nom ou la distance a mal été saisie")
            
        else:
            for acteur in ensemble_proche:
                self.textboxEnsemble.insert("0.0","\""+acteur+"\""+"\n")
            self.textboxEnsemble.insert("0.0","les acteurs à x distance")
            
        self.textboxEnsemble.configure(state="disabled")
        

        
class PopupActeurcommun(customtkinter.CTk):
    def __init__(self,Listecommun):
        super().__init__()
        
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # configure window
        self.title("liste des acteurs communs")
        self.geometry(f"{300}x{300}")
        self.textboxEnsemble = customtkinter.CTkTextbox(self, width=250)
        self.textboxEnsemble.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        for acteur in Listecommun:
            self.textboxEnsemble.insert("0.0","\""+str(acteur)+"\""+"\n")   
        self.textboxEnsemble.insert("0.0","liste des acteurs communs"+"\n")      
        self.textboxEnsemble.configure(state="disabled")
                
        
        
        
#__________________________classe de la cration des raduo boutton _____________________________________________________________________   
#___________________________________________________________________________________________________________________________   
 

class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="snew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=i, variable=self.variable) #on affecte a un boutton un numero qui sera utiliser 
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="snew")                   #pour la sous fonction option
            self.radiobuttons.append(radiobutton)
    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   
         



class App(customtkinter.CTk):
    
        
    def __init__(self):
        super().__init__()

        # configuration ecran
        self.title("App GRAPHE SAE 2.02")
        self.geometry(f"{1060}x{550}")

        self.grid_columnconfigure(3, weight=0)

        
        self.grid_rowconfigure((0,2), weight=1)
        self.grid_rowconfigure((3), weight=1)
        self.grid_rowconfigure((1), weight=0)


#_______________________________________creation des sidebar pour separer les partie des widgets____________________________________________________   
#___________________________________________________________________________________________________________________________   

        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        
        self.sidebar_frame6 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame6.grid(row=0, column=1, sticky="new",padx=(20, 20))
        self.sidebar_frame6.configure(fg_color="transparent")   
        
        self.sidebar_frame2 = customtkinter.CTkFrame(self.sidebar_frame6, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=0, sticky="new",pady=(20, 0))

        self.sidebar_frame2.configure(fg_color="transparent")
        
        
        self.sidebar_frame3 = customtkinter.CTkFrame(self.sidebar_frame6, width=140, corner_radius=0)
        self.sidebar_frame3.grid(row=1, column=0, sticky="new")

        self.sidebar_frame3.configure(fg_color="transparent")
        
        
        self.sidebar_frame4 = customtkinter.CTkFrame(self.sidebar_frame6, width=140, corner_radius=0)
        self.sidebar_frame4.grid(row=2, column=0, sticky="new")

        self.sidebar_frame4.configure(fg_color="transparent")
        
        self.sidebar_frame5 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame5.grid(row=1, column=1, sticky="new",padx=(20, 20), columnspan=3)
        self.sidebar_frame5.configure(fg_color="transparent")        
      
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   
     
        

#_______________________________________premiere ranger de boutton partie creation des bouttons _________________________________________________________   
#___________________________________________________________________________________________________________________________   

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #afficher graph integral
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="afficher graph integral", command=self.afficher_graph_integral)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10,sticky="nesw")
        
        
        #sauvegarde le graph en png
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="sauvegarder", command=self.afficher_et_sauvegarderdata)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10,sticky="nesw")
        
        
        #sousgraphe
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="sous-graphe de chaque film", command=self.sousgraphe)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10,sticky="nesw")
        
        
        
        #ensemblesActeur
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="listes des acteurs presents", command=self.ensemblesActeur)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10,sticky="nesw")
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   

        
        
        
        
        
        
 #____________________________________________entrer de la ACTEUR A + son titre_________________________________________________________          
#___________________________________________________________________________________________________________________________    
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame2, text="ACTEUR A", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="nsew")
        

        self.entryA = customtkinter.CTkEntry(self.sidebar_frame2, placeholder_text="entrez un acteur")
        self.entryA.grid(row=1, column=1, padx=20, pady=5,sticky="new")#state = entry.get()
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   

 

#______________________________________entrer de la ACTEUR B + son titre________________________________________________________________          
#___________________________________________________________________________________________________________________________    

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame3, text="ACTEUR B", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=3, column=1, padx=10, pady=(10, 5), sticky="nsew")


        self.entryB = customtkinter.CTkEntry(self.sidebar_frame3, placeholder_text="entrez un acteur")
        self.entryB.grid(row=4, column=1,padx=20, pady=5, sticky="nsew")
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   




#_____________________________________entrer de la distance + son titre________________________________________________________________   
#___________________________________________________________________________________________________________________________   

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame4, text="DISTANCE", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=3, column=1, padx=10, pady=(10, 5), sticky="nsew")


        self.entryC = customtkinter.CTkEntry(self.sidebar_frame4, placeholder_text="entrez une Distance")
        self.entryC.grid(row=4, column=1,padx=20, pady=(10,20), sticky="nsew")#state = entry.get()
#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   




#______________________________________________jeux de boutton Fonctionaliter________________________________________          
#___________________________________________________________________________________________________________________________    

        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame5, text="Fonctionnalités", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=2, padx=20, pady=(20, 10))

                
           #collaborateurs_communs     
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame5, text="collaborateurs_communs", command=self.collaborateurcom)
        self.sidebar_button_5.grid(row=1, column=0, padx=20, pady=10)
        
           #collaborateurs_proches
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame5,text="collaborateurs_proches", command=self.collaboproches)
        self.sidebar_button_6.grid(row=1, column=1, padx=20, pady=10)
        
        
            #button distance
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame5,text="distance", command=self.distance)
        self.sidebar_button_7.grid(row=1, column=2, padx=20, pady=10)
        
        #boutton centraliter
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame5,text="centralite", command=self.Bouton_centralite)
        self.sidebar_button_8.grid(row=1, column=3, padx=20, pady=10)





#_______________________affichage dark mode puis text box pour le manuel et pour finir radioboutton des option d'affichage____________________________________________________          
#___________________________________________________________________________________________________________________________    

        
        #affichage dark mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(20, 20))
        

        # create pour le manuel
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        self.textbox.insert("0.0", "Manuel\n\n" + "explication du programmes.\n\n"+"les boutons à gauche son pour afficher directement le graphe complet Sauvegarder une PDG le graphe intégral "+"\n"+"\n"+"elle peut afficher le graphe complet \n avec différents types d’affichage en fonction de l’option choisit"+"\n"+"\n"+"On peut rentrer les paramètres : acteur A, \nacteur B, une distance. Ainsi, on peut choisir : "+"\n"+"- la distance entre deux acteurs,"+"\n"+"- les acteur communs aux deux,"+"\n"+"- pour une distance choisie tous les acteurs proches de l’acteur,"+"\n"+"- la distance la plus proche entre l’acteur A et B,"+"\n"+"- et, pour finir, la centralité"+"\n")
        self.textbox.configure(state="disabled")

    
        # create radioboutton des option d'affichage
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options affichage graph", values=["option 1", "option 2","option 3","option 4","option 5"])
        self.radiobutton_frame.grid(row=0, column=3, padx=(0, 10), pady=(20, 0), sticky="nsew")


        # set default values

        self.appearance_mode_optionemenu.set("Light")
#___________________________________________________________________________________________________________________________          
#___________________________________________________________________________________________________________________________    
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def collaboproches(self):
        a=self.entryA.get()
        c=self.entryC.get()
        try:
            c = int(c)
        except:
            c=0
        ensemble_proche=requetes.collaborateurs_proches(sous_fonction.G,a,c)
        Popup = oracle.Popupestproche(ensemble_proche)
        Popup.mainloop()
        
        
    def collaborateurcom(self):
        a=self.entryA.get()
        b=self.entryB.get()
        Ensemble=requetes.collaborateurs_communs(sous_fonction.G,a,b)
        print(Ensemble)
        Popup = oracle.PopupActeurcommun(Ensemble)
        Popup.mainloop() 
        print('stop')
        return None
            
    
    def distance(self):
        a=self.entryA.get()
        b=self.entryB.get()
        
        distanceparcourus=requetes.distance(sous_fonction.G,a,b)
        Popup = oracle.distancePOUPUP(distanceparcourus)
        Popup.mainloop()
        
        
        
        
    def ensemblesActeur(self):
        Popup = oracle.Popup(sous_fonction.E)
        Popup.mainloop() 
        print('stop')
        return None
    
    def Bouton_centralite(self):
        a=self.entryA.get()
        distance_centralite=requetes.centralite(sous_fonction.G,a)
        distance_centralite= int(distance_centralite)
        Popup = oracle.Popupcentralite(distance_centralite)
        Popup.mainloop() 
        print('stop')
        return None
        
        
        
    def afficher_graph_integral(self):
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
        sous_fonction.montrer_graph(sous_fonction.G,x)


    def afficher_et_sauvegarderdata(self):
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
        sous_fonction.afficher_et_sauvegarder(sous_fonction.G,x)

    def sousgraphe(self):
        f=False
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
            
        self.sidebar_button_3.configure(state="disabled")         
           
        f=sous_fonction.sousgraphe_PAR_FILM(sous_fonction.D,x)
        
        if f == True:
            self.sidebar_button_3.configure(state="standard")
        
        
    def idk(self):
        on = False
        on = not on
        
        
   



        
if __name__ == "__main__":
    app = App()
    app.mainloop()
         
        
    

        

    











