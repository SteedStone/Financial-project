import tkinter
import tkinter.messagebox
import customtkinter
import Appli_copy as Ap
import numpy 


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Calculateur")
        self.geometry(f"{1100}x{800}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        #self.textbox = customtkinter.CTkTextbox(self, width=250)
        #self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def login(): 

            username = "Geeks"
            password = "12345"
             

             

            if self.user_entry.get() == username and self.user_pass.get() == password: 
                self.tabview = customtkinter.CTkTabview(self)
                self.tabview.grid(row=0, column=1, padx=(10, 20), pady=(5, 0), sticky="nsew")
                self.tabview.add("FTP rates")
                self.tabview.add("FTP option")
                self.tabview.add("FTP LP")
                self.tabview.add("FTP cos")
                self.tabview.tab("FTP rates").grid_columnconfigure(0, weight=0)  # configure grid of individual tabs
                self.tabview.tab("FTP option").grid_columnconfigure(0, weight=1)

                #Entrée une 
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Nombre de periodes")
                self.scaling_label.grid(row=0, column=3, padx=20, pady=(0, 5))
                self.entry = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")
                #entrée deux 
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Montant d'emprun")
                self.scaling_label.grid(row=1, column=3, padx=20, pady=(0, 5))
                self.entry1 = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry1.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")
                #Entrée trois 
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Taux d'intérêts annuel")
                self.scaling_label.grid(row=2, column=3, padx=20, pady=(0, 5))
                self.entry2 = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry2.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")
                #Entrée quztre 
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Prepayment")
                self.scaling_label.grid(row=3, column=3, padx=20, pady=(0, 5))
                self.entry3 = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry3.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")
                #Entrée cinq
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Nombre de payment par an")
                self.scaling_label.grid(row=4, column=3, padx=20, pady=(0, 5))
                self.entry4 = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry4.grid(row=4, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")
                #Entrée Six
                self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text="Duree repracing")
                self.scaling_label.grid(row=5, column=3, padx=20, pady=(0, 5))
                self.entry5 = customtkinter.CTkEntry(self.tabview.tab("FTP rates"), placeholder_text="")
                self.entry5.grid(row=5, column=1, columnspan=2, padx=(20, 0), pady=(0, 5), sticky="nsew")


                self.main_button_1 = customtkinter.CTkButton(master=self.tabview.tab("FTP rates"), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.button_event,text="Calculer l'AS")
                self.main_button_1.grid(row=6, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

            elif self.user_entry.get() == username and self.user_pass.get() != password: 
                tkinter.messagebox.showwarning(title='Wrong password',message='Please check your password') 
            elif self.user_entry.get() != username and self.user_pass.get() == password: 
                tkinter.messagebox.showwarning(title='Wrong username',message='Please check your username') 
            else: 
                tkinter.messagebox.showerror(title="Login Failed",message="Invalid Username and password") 
        
        
        #Login username and Mots de passse 
        self.frame = customtkinter.CTkFrame(self) 
        self.frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 
        self.frame.grid_columnconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(master=self.frame,text='Modern Login System UI') 
        self.label.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")  


        self.user_entry= customtkinter.CTkEntry(master=self.frame,placeholder_text="Username") 
        self.user_entry.grid(row=2, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 

        self.user_pass= customtkinter.CTkEntry(master=self.frame,placeholder_text="Password",show="*") 
        self.user_pass.grid(row=3, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 


        button = customtkinter.CTkButton(master=self.frame,text='Login',command=login) 
        button.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")  

        




        

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create premier rectangle
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Individual Pricing")
        self.scrollable_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.scrollable_frame_switches = []

        self.scaling_label = customtkinter.CTkLabel(self.scrollable_frame, text="Type")
        self.scaling_label.grid(row=0, column=1, padx=5, pady=(0, 10))
        switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Fixed/Float ")
        switch.grid(row=0, column=0, padx=10, pady=(0, 10))
        self.scrollable_frame_switches.append(switch)

        

        self.scaling_label = customtkinter.CTkLabel(self.scrollable_frame, text="T")
        self.scaling_label.grid(row=1, column=1, padx=5, pady=(0, 10))
        self.slider_4 = customtkinter.CTkSlider(self.scrollable_frame, from_=0, to=1, number_of_steps=6 )
        self.slider_4.grid(row=1, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        

        self.scaling_label = customtkinter.CTkLabel(self.scrollable_frame, text="Frequence")
        self.scaling_label.grid(row=2, column=1, padx=5, pady=(0, 10))
        self.optionmenu = customtkinter.CTkOptionMenu(self.scrollable_frame, dynamic_resizing=False,
                                                        values=["1/1/1", "5/5/5", "10/5/5" , "20/5/5"])
        self.optionmenu.grid(row=2, column=0, padx=20, pady=(20, 10))

        self.optionmenu.set("")

        self.scaling_label = customtkinter.CTkLabel(self.scrollable_frame, text="Cap")
        self.scaling_label.grid(row=3, column=1, padx=5, pady=(0, 10))
        self.combobox = customtkinter.CTkComboBox(self.scrollable_frame,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.combobox.set("")

        


        

       
        
        
        
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Entrez le nombre de périodes :", title="CTkInputDialog")
        
        print(dialog.get_input())
        
    

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def button_event(self):
        print(self.entry.get())
        print(self.entry1.get())
        nb_periodes = int(self.entry.get())
        montant_emprunt = int(self.entry1.get())
        taux_interet_annuel = float(self.entry2.get())
        prepayment = float(self.entry3.get())  # Convertir en float si nécessaire
        nombre_de_payment_par_an = int(self.entry4.get())
        Duree_repracing_anne = int(self.entry5.get())
        per = 1
        param = Ap.Parametres(nb_periodes, montant_emprunt, taux_interet_annuel, prepayment, nombre_de_payment_par_an, Duree_repracing_anne, per)
        chemin_fichier = r"C:\Users\guera\OneDrive - UCL\Bureau\Papa\Calcul Hedging_Rates_BBG_based_NEW_INCL_SECUR_Factor_V2.2_frozen.xlsm"

        # Création des instances
        gestion_fichier = Ap.GestionFichier(chemin_fichier)
        calculs = Ap.Calculs(param, gestion_fichier)
        print("Résultat du calcul :", calculs.retourne_valeurs_attendue())

        Resultat = calculs.retourne_valeurs_attendue()
        self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text=str(Resultat))
        self.scaling_label.grid(row=7, column=3, padx=20, pady=(0, 5))

    


app = App()
app.mainloop()