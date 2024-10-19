import tkinter

import customtkinter

import requet
import networkx as nx
import matplotlib.pyplot as plt
import requet
import oracle





customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



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
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=i, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="snew")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
        



class App(customtkinter.CTk):
    
        
    def __init__(self):
        super().__init__()

        # configure window
        self.title("App GRAPHE SAE 2.02")
        self.geometry(f"{1060}x{550}")

        # configure grid layout (4x4)
        #self.grid_columnconfigure((), weight=1)
        self.grid_columnconfigure(3, weight=0)

        
        self.grid_rowconfigure((0,2), weight=1)
        self.grid_rowconfigure((3), weight=1)
        self.grid_rowconfigure((1), weight=0)

        # create sidebar frame with widgets

        
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
        

        
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="afficher graph integral", command=self.afficher_graph_integral)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10,sticky="nesw")
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="sauvegarder", command=self.afficher_et_sauvegarderdata)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10,sticky="nesw")
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="sous-graphe", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10,sticky="nesw")
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="afficher graph", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10,sticky="nesw")
        
 #___________________________________________________________________________________________________________________________          
#___________________________________________________________________________________________________________________________    
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame2, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="nsew")
        

        self.entry = customtkinter.CTkEntry(self.sidebar_frame2, placeholder_text="entrer un acteur")
        self.entry.grid(row=1, column=1, padx=20, pady=5,sticky="new")#state = entry.get()

        self.main_button_1 = customtkinter.CTkButton(master=self.sidebar_frame2, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="entrer")
        self.main_button_1.grid(row=2, column=1,padx=20, pady=5, sticky="nsew")

#___________________________________________________________________________________________________________________________          
#___________________________________________________________________________________________________________________________    

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame3, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=3, column=1, padx=10, pady=(10, 5), sticky="nsew")


        self.entry = customtkinter.CTkEntry(self.sidebar_frame3, placeholder_text="entrer un acteur")
        self.entry.grid(row=4, column=1,padx=20, pady=5, sticky="nsew")#state = entry.get()

        self.main_button_1 = customtkinter.CTkButton(master=self.sidebar_frame3, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="entrer")
        self.main_button_1.grid(row=5, column=1,padx=20, pady=(5,20), sticky="nsew")

#___________________________________________________________________________________________________________________________   
#___________________________________________________________________________________________________________________________   

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame4, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=3, column=1, padx=10, pady=(10, 5), sticky="nsew")


        self.entry = customtkinter.CTkEntry(self.sidebar_frame4, placeholder_text="entrer un acteur")
        self.entry.grid(row=4, column=1,padx=20, pady=(10,20), sticky="nsew")#state = entry.get()

        self.main_button_1 = customtkinter.CTkButton(master=self.sidebar_frame4, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="entrer")
        self.main_button_1.grid(row=5, column=1,padx=20, pady=(5,20), sticky="nsew")



#___________________________________________________________________________________________________________________________          
#___________________________________________________________________________________________________________________________    

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame5, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=2, padx=20, pady=(20, 10))

                
                
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame5, text="collaborateurs_communs", command=self.afficher_graph_integral)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame5,text="collaborateurs_proches", command=self.afficher_et_sauvegarderdata)
        self.sidebar_button_2.grid(row=1, column=1, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame5,text="distance", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=1, column=2, padx=20, pady=10)
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame5,text="centralite", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=1, column=3, padx=20, pady=10)

#___________________________________________________________________________________________________________________________          
#___________________________________________________________________________________________________________________________    

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(20, 20))
        

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")  
        self.textbox.insert("0.0", "Manuel\n\n" + "explication du programmes.\n\n"+"les boutons à gauche son pour afficher directement le graphe complet Sauvegarder une PDG le graphe intégral "+"\n"+"Afficher l'integraliter des sous-graphe"+"\n"+"\n"+"Une option permet de différentier l'affichage En cercle , normal et autres"+"\n"+"La distance simple est dure. Son soit la distance simple ou naïve"
+"\n"+"\n"+"Pour chercher l'ensemble des personne commune à un acteur taper juste l'acteur Prénom et nom "+"\n"+"puis appuyer sur entrer le bouton"+"\n"+"Exemple" +"\n"+"\n"+"Albert Henderson"+"\n"+"\n"+"Pour mettre une distance la meme chose mais avec  ,nombre"+"\n"+"Exemple"+"\n"+"\n"+"Albert Henderson,3\n\n"+"Pour la plus grande connexion taper eloignementmax\n"+"\n\ntapper centre+nom+prenom1+nom+prenom2 \nce qui represente la plus grande distance qui le sépare d’un autre acteur a un autre \n\n")
        self.textbox.configure(state="disabled")

    
        # create radiobutton frame
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options affichage graph", values=["option 1", "option 2","option 3","option 4","option 5"])
        self.radiobutton_frame.grid(row=0, column=3, padx=(0, 10), pady=(20, 0), sticky="nsew")


        # set default values

        self.appearance_mode_optionemenu.set("Light")
      


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


        
    def afficher_graph_integral(self):
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
        oracle.montrer_graph(oracle.G,x)


    def afficher_et_sauvegarderdata(self):
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
        oracle.afficher_et_sauvegarder(oracle.G,x)

    def sidebar_button_event(self):
        try:
            x = self.radiobutton_frame.get()
            x = int(x)
        except:
            x = int(0)
        oracle.sousgraphe_PAR_FILM(oracle.D,x)
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()
         
        
    
    
    











