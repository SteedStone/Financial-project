import tkinter 
import tkinter.messagebox
import customtkinter
import Backup.Appli_copy as Ap
import numpy 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import threading



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class TableauResume(customtkinter.CTkFrame):
    def __init__(self,  parent, MortGage, FTPS,bol, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.MortGage = MortGage
        self.FTPS = FTPS
        self.bol = bol
        self.value = {}
        self.Mortgage_FTPS = {
            ("10Y - 1/1/1", "FTP Rates"): "-",
            ("15Y - 1/1/1", "FTP Rates"): "-",
            ("20Y - 1/1/1", "FTP Rates"): "-",
            ("10Y - 5/5/5", "FTP Rates"): "-",
            ("15Y - 5/5/5", "FTP Rates"): "-",
            ("20Y - 5/5/5", "FTP Rates"): "-",
            ("25Y - 5/5/5", "FTP Rates"): "-",
            ("25Y - 10/5/5", "FTP Rates"): "-",
            ("25Y - 20/5/5", "FTP Rates"): "-",
            ("5Y - FIX", "FTP Rates"): "-",
            ("10Y - FIX", "FTP Rates"): "-",
            ("13Y - FIX", "FTP Rates"): "-",
            ("15Y - FIX", "FTP Rates"): "-",
            ("18Y - FIX", "FTP Rates"): "-",
            ("20Y - FIX", "FTP Rates"): "-",
            ("25Y - FIX", "FTP Rates"): "-",
            ("30Y - FIX", "FTP Rates"): "-"
            # Ajoutez les autres prix ici
        }
        self.create_tableau()
        

    def create_tableau(self):
        # Créer les en-têtes des colonnes
        if self.bol == True : 
            self.start_init_valeur()
        else : 
            self.update_tableau()

    def start_init_valeur(self) : 
        thread = threading.Thread(target=self.init_valeur)
        thread.start()
    def init_valeur(self) : 
            for cle in self.Mortgage_FTPS : 
                print(cle)
                elements = cle[0].split()
                premier_element = elements[0]
                nmb_Periode = int(premier_element[:-1]) * 12
                if "FIX" in elements : 
                    duree_rpracing = 100
                else : 
                    duree_rpracing = int(elements[2].split('/')[0])
                    print(duree_rpracing)
                # Taux is useless because it is reassigned later in the function
                taux=0
                print(nmb_Periode)
                print(duree_rpracing)
                self.Mortgage_FTPS[cle] = str(self.parent.donne_resultat(nmb_Periode,taux , duree_rpracing))
            self.after(0, self.update_tableau())
                

    def update_tableau(self ):
        customtkinter.CTkLabel(self, text="Mortgage").grid(row=0, column=0, sticky="nsew")
        for i, magasin in enumerate(self.FTPS, start=1):
            customtkinter.CTkLabel(self, text=magasin).grid(row=0, column=i, sticky="nsew")

        # Remplir le tableau avec les données
        for i, fruit in enumerate(self.MortGage, start=1):
            customtkinter.CTkLabel(self, text=fruit).grid(row=i, column=0, sticky="nsew")
            for j in range(1, len(self.FTPS) + 1):
                prix = self.get_prix(fruit, self.FTPS[j - 1])  # Obtenir le prix du fruit dans le magasin actuel
                customtkinter.CTkLabel(self, text=prix).grid(row=i, column=j, sticky="nsew")

        # Ajuster les poids des colonnes et des lignes pour permettre le redimensionnement
        for i in range(len(self.FTPS) + 1):
            self.grid_columnconfigure(i, weight=1)
        for i in range(len(self.MortGage) + 1):
            self.grid_rowconfigure(i, weight=1)
    def get_prix(self, Mortgage, FTPS ):
        # Simulation de la fonction pour obtenir le prix du fruit dans le magasin spécifié
        # Ici, nous supposerons que nous avons une liste de prix pour chaque fruit dans chaque magasin
        # et nous y accéderons avec des clés fruit-magasin
        return self.Mortgage_FTPS.get((Mortgage, FTPS), "-")

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()
        self.selected_file_path = None
        self.freq_present = True 
        
        # configure window
        self.title("Calculateur")
        self.geometry(f"{1100}x{800}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.Mortgage = ["10Y - 1/1/1","15Y - 1/1/1","20Y - 1/1/1","10Y - 5/5/5","15Y - 5/5/5", "20Y - 5/5/5", "25Y - 5/5/5", "25Y - 10/5/5","25Y - 20/5/5","5Y - FIX","10Y - FIX",
            "13Y - FIX", 
            "15Y - FIX", 
            "18Y - FIX",
            "20Y - FIX", 
            "25Y - FIX", 
            "30Y - FIX"]
        
        self.FTP = ["FTP Rates", "FTP Option"]

        
    
        

        

        
        #Ext button
        self.exit_button()
        
        #Premiere box 
        self.First_box()
        #Deuxième box 
        self.Second_box()

        self.third_box(bol = False)
        self.resulat_boutton()
        

        
                




        

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

        
        
        


        

       
        
        
        
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")
    def exit_button(self) : 
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text = "Exit",width=0.1,command=self.log_out)
        self.main_button_1.grid(row=3, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
    def resulat_boutton(self) : 
        button_frame = customtkinter.CTkFrame(self)
        button_frame.grid(row=3, column=1, pady=(10, 10), sticky="nsew")

        # Bouton Compute
        self.main_button_2 = customtkinter.CTkButton(master=button_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Compute", width=0.1, command=lambda: self.third_box(bol=True))
        self.main_button_2.pack(side="left", padx=(0, 10))

        # Bouton Generate PDF
        self.main_button_3 = customtkinter.CTkButton(master=button_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Generate PDF", width=0.1,command=self.generate_pdf)
        self.main_button_3.pack(side="right", padx=(0, 10))
    def First_box(self) : 
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Individual Pricing Parameter")
        self.scrollable_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.scrollable_frame_switches = []

        self.scaling_label1 = customtkinter.CTkLabel(self.scrollable_frame, text="Type")
        self.scaling_label1.grid(row=0, column=1, padx=5, pady=(0, 10))
        self.switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Fixed/Float ",variable=customtkinter.BooleanVar(value=True))
        self.switch.grid(row=0, column=0, padx=10, pady=(0, 10))
        self.scrollable_frame_switches.append(self.switch)

        #Frequence selon la position du fixed float
        self.last_switch_state = self.switch.get()
        self.check_switch_state()
        self.add_frequence()
        
        #Frequence selon la position du fixed float
        self.scaling_label2 = customtkinter.CTkLabel(self.scrollable_frame, text="T = 0")
        self.scaling_label2.grid(row=1, column=1, padx=5, pady=(0, 10))
        self.slider_4 = customtkinter.CTkSlider(self.scrollable_frame, from_=0, to=30, number_of_steps=30,command = self.update_label )
        self.slider_4.grid(row=1, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        
        self.get_value_slider = self.slider_4.get()
        

        

        self.scaling_label3 = customtkinter.CTkLabel(self.scrollable_frame, text="Cap")
        self.scaling_label3.grid(row=3, column=1, padx=5, pady=(0, 10))
        self.combobox = customtkinter.CTkComboBox(self.scrollable_frame,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.combobox.set("")


        self.scaling_label4 = customtkinter.CTkLabel(self.scrollable_frame, text="Load file")
        self.scaling_label4.grid(row=4, column=1, padx=5, pady=(0, 10))
        select_file_button = customtkinter.CTkButton(self.scrollable_frame, text="Excel", command=self.select_file)
        select_file_button.grid(row=4, column = 0,padx=5, pady=(10,10))

        self.scaling_label = customtkinter.CTkLabel(self.scrollable_frame, text="Taux d'intérêts\n annuel")
        self.scaling_label.grid(row=5, column=1, padx=5, pady=(0, 10))
        self.entry2 = customtkinter.CTkEntry(self.scrollable_frame, placeholder_text="")
        self.entry2.grid(row=5, column=0, padx=5, pady=(10, 10)) 
        
    def Second_box(self) : 
        self.frame = customtkinter.CTkFrame(self) 
        self.frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 
        self.frame.grid_columnconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(master=self.frame,text='Access for Olivier Dewell') 
        self.label.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")  


        self.user_entry= customtkinter.CTkEntry(master=self.frame,placeholder_text="Username") 
        self.user_entry.grid(row=2, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 

        self.user_pass= customtkinter.CTkEntry(master=self.frame,placeholder_text="Password",show="*") 
        self.user_pass.grid(row=3, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 


        button = customtkinter.CTkButton(master=self.frame,text='Login',command=self.login) 
        button.grid(row=5, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 

    def second_box_after_login(self) : 
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=1, padx=(10, 20), pady=(5, 0), sticky="nsew")
        self.tabview.add("FTP rates")
        self.tabview.add("FTP option")                
        self.tabview.add("FTP LP")
        self.tabview.add("FTP cos")
        self.tabview.tab("FTP rates").grid_columnconfigure(0, weight=0)  # configure grid of individual tabs            self.tabview.tab("FTP option").grid_columnconfigure(0, weight=1)


        self.main_button_1 = customtkinter.CTkButton(master=self.tabview.tab("FTP rates"), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.button_event,text="Calculer l'AS")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def third_box(self , bol) : 
        

        self.graphical = TableauResume(self , self.Mortgage , self.FTP , bol ) 
        self.graphical.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew" ) 
        self.graphical.grid_columnconfigure(1, weight=1)
        
    
    

    def generate_pdf(self):
        # Nom du fichier PDF
        pdf_file = "tableau_resume.pdf"

        # Création du canvas PDF
        c = canvas.Canvas(pdf_file, pagesize=letter)
        
        # Position initiale
        x_offset = 100
        y_offset = 700
        line_height = 20
        
        # Ajout du titre
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x_offset, y_offset, "Tableau Résumé")
        c.setFont("Helvetica", 12)
        
        # Ajout du contenu de la troisième boîte
        y_offset -= line_height
        for row in range(self.graphical.grid_size()[1]):
            for column in range(self.graphical.grid_size()[0]):
                widget = self.graphical.grid_slaves(row, column)
                if widget:
                    text = widget[0].cget("text")
                    c.drawString(x_offset + column * 100, y_offset - row * line_height, text)

        # Sauvegarde du PDF
        c.save()

        print(f"PDF généré avec succès : {pdf_file}")

    
    def login(self) : 
    

        username = "Geeks"
        password = "12345"
             

            

        if self.user_entry.get() == username and self.user_pass.get() == password: 
            self.second_box_after_login()
            

        elif self.user_entry.get() == username and self.user_pass.get() != password: 
            tkinter.messagebox.showwarning(title='Wrong password',message='Please check your password') 
        elif self.user_entry.get() != username and self.user_pass.get() == password: 
            tkinter.messagebox.showwarning(title='Wrong username',message='Please check your username') 
        else: 
            tkinter.messagebox.showerror(title="Login Failed",message="Invalid Username and password") 
    
    
    

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def select_file(self):
        self.selected_file_path = tkinter.filedialog.askopenfilename()
        if self.selected_file_path:
            print("Fichier sélectionné :", self.selected_file_path)
            # Vous pouvez appeler une fonction de traitement ici ou utiliser selected_file_path ailleurs dans votre programme


    def button_event(self):
        
        
        nb_periodes = int(self.get_value_slider * 12) + 5
        print(self.get_value_slider)
        taux_interet_annuel = float(self.entry2.get())

        param = Ap.Parametres(nb_periodes, taux_interet_annuel, self.Duree_repracing_anne)
        if self.selected_file_path != None and self.Duree_repracing_anne != None: 
            self.chemin_fichier = rf"{self.selected_file_path}"
            # Création des instances
            self.gestion_fichier = Ap.GestionFichier(self.chemin_fichier)
            calculs = Ap.Calculs(param, self.gestion_fichier)
            print("Résultat du calcul :", calculs.retourne_valeurs_attendue())

            Resultat = calculs.retourne_valeurs_attendue()
            self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("FTP rates"), text=str(Resultat))
            self.scaling_label.grid(row=7, column=3, padx=20, pady=(0, 5))
        else : 
            tkinter.messagebox.showwarning(title='Missing parameters',message='Please enter the correct param') 
    

    
    
    
    
    def log_out(self) : 
        self.destroy()
    def check_switch_state(self):
        
        switch_state = self.switch.get()
        if switch_state != self.last_switch_state:
            self.last_switch_state = switch_state
            if switch_state:
                self.add_frequence()
            else:
                self.remove_frequence()
                self.Duree_repracing_anne = 100
        self.after(100, self.check_switch_state)  # Vérifiez l'état du switch toutes les 100 ms
    def remove_frequence(self):
            self.freq_present = False 
    # Supprimer le CTkLabel
            self.scaling_label5.grid_remove()
            self.scaling_label5.destroy()
            del self.scaling_label5

        # Supprimer le CTkOptionMenu
            self.optionmenu5.grid_remove()
            self.optionmenu5.destroy()
            del self.optionmenu5
    def add_frequence(self) : 
        self.freq_present = True
        self.scaling_label5 = customtkinter.CTkLabel(self.scrollable_frame, text="Frequence")
        self.scaling_label5.grid(row=2, column=1, padx=5, pady=(0, 10))
        self.optionmenu5 = customtkinter.CTkOptionMenu(self.scrollable_frame, dynamic_resizing=False,
                                                        values=["1/1/1", "5/5/5", "10/5/5" , "20/5/5"], )
        self.optionmenu5.grid(row=2, column=0, padx=20, pady=(0, 10))

        self.optionmenu5.set("")
        
        self.last_value1 = self.optionmenu5.get()
        self.check_option_menu_5()

    def check_option_menu_5(self) :
        
        if self.freq_present == True : 
            last_value2 = self.optionmenu5.get()
            if last_value2 != self.last_value1:
                self.last_value1 = last_value2
                if last_value2 == "1/1/1":
                    self.Duree_repracing_anne = 1
                elif last_value2 == "5/5/5":
                    self.Duree_repracing_anne = 5
                elif last_value2 == "10/5/5" : 
                    self.Duree_repracing_anne = 10
                elif last_value2 == "20/5/5":
                    self.Duree_repracing_anne = 20
                else : 
                    pass
            self.after(100, self.check_option_menu_5)  # Vérifiez l'état du switch toutes les 100 ms
    def update_label(self,value):
        self.scaling_label2.configure(text = f"T = {int(value)}")
    def donne_resultat(self , nb_periodes , taux_interet_annuel , Duree_repracing_anne) : 
        taux_interet_annuel = float(self.entry2.get())
        param = Ap.Parametres(nb_periodes, taux_interet_annuel, Duree_repracing_anne)
        if self.selected_file_path != None : 
            self.chemin_fichier = rf"{self.selected_file_path}"
            # Création des instances
            gestion_fichier = Ap.GestionFichier(self.chemin_fichier)
            calculs = Ap.Calculs(param, gestion_fichier)
            resultat = calculs.retourne_valeurs_attendue()
            resultat_arrondis = round(resultat , 3)
            print("Résultat du calcul :", resultat_arrondis)

            return resultat_arrondis
            
         

    


app = App()
app.mainloop()