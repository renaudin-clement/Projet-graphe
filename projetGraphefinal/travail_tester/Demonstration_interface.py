import tkinter

import customtkinter

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
        self.geometry(f"{1060}x{500}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)

        
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=0)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="GRAPHEMAKER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="afficher graph integral", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="sauvegarder", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="sous-graphe", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="afficher graph", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)



        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(20, 20))
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="entrer un acteur")
        self.entry.grid(row=2, column=1, sticky="nsew")#state = entry.get()

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="entrer")
        self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Manuel\n\n" + "explication du programmes.\n\n"+"les boutons à gauche son pour afficher directement le graphe complet Sauvegarder une PDG le graphe intégral "+"\n"+"Afficher l'integraliter des sous-graphe"+"\n"+"\n"+"Une option permet de différentier l'affichage En cercle , normal et autres"+"\n"+"La distance simple est dure. Son soit la distance simple ou naïve"
+"\n"+"\n"+"Pour chercher l'ensemble des personne commune à un acteur taper juste l'acteur Prénom et nom "+"\n"+"puis appuyer sur entrer le bouton"+"\n"+"Exemple" +"\n"+"\n"+"Albert Henderson"+"\n"+"\n"+"Pour mettre une distance la meme chose mais avec  ,nombre"+"\n"+"Exemple"+"\n"+"\n"+"Albert Henderson,3\n\n"+"Pour la plus grande connexion taper eloignementmax\n"+"\n\ntapper centre+nom+prenom1+nom+prenom2 \nce qui represente la plus grande distance qui le sépare d’un autre acteur a un autre \n\n")
        self.textbox.configure(state="disabled")
        
    
        # create radiobutton frame
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options affichage graph", values=["option 1", "option 2","option 3","option 4"])
        self.radiobutton_frame.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="nsew")

        
        
        
        



        # 
        self.choix_methode = customtkinter.CTkFrame(self, fg_color="transparent")
        self.choix_methode.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.choix_methode.grid_columnconfigure(0, weight=1)
        self.choix_methode.grid_rowconfigure(4, weight=1)
        
        
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.choix_methode)
        self.seg_button_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="nsew")
        




        # set default values



        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
       
        
        self.seg_button_1.configure(values=["distance dure", "distance simple"])
        self.seg_button_1.set("Value 2")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def button_callback(self):

        print("checkbox_frame_2:", self.radio_button_1.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
