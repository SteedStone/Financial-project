import pandas as pd
import numpy as np 
import numpy_financial as npf


class Parametres:
    def __init__(self, Nombre_de_periodes, taux_interet_annuel, Duree_repracing_anne):
        self.Nombre_de_periodes = Nombre_de_periodes
        self.taux_interet_annuel = taux_interet_annuel
        self.Duree_repracing_anne = Duree_repracing_anne
        



class GestionFichier:
    def __init__(self, chemin_fichier):
        self.data = pd.read_excel(chemin_fichier, engine="openpyxl", sheet_name='BBG rates', skiprows=1)

class Calculs:
    def __init__(self, parametres, gestion_fichier):
        self.parametres = parametres
        self.gestion_fichier = gestion_fichier

    
     
    def retourne_valeurs_attendue(self) : 
            # Param that won't change
            montant_emprunt = 10000000
            prepayment = 0.04
            nombre_de_payment_par_an = 12
            per = 1

            # Param that will change
            Nombre_de_periodes = self.parametres.Nombre_de_periodes
            taux_interet_annuel = self.parametres.taux_interet_annuel
            Duree_repracing_anne = self.parametres.Duree_repracing_anne
            data = self.gestion_fichier.data 
            
            Periodical_basis = (1 + taux_interet_annuel) ** (1 / nombre_de_payment_par_an) - 1
            #print(Periodical_basis)
            
            Periodical_basis_2 = (1 + prepayment) ** (1 / nombre_de_payment_par_an) - 1
            #print(Periodical_basis_2)
            array = np.random.rand(30,361)
            array[0] = np.arange(0, 361)
            array[1] = np.arange(0,180.5,0.5)
            array[2] = np.arange(0,90.25,0.25)
            array[3] = array[0]/12
            array[4] = np.zeros(361)

            for i in range(5,14) : 
                  array[i] = np.zeros(361)
                  array[i][0] = 0
            array[14] = np.zeros(361)
            ColonneR = np.arange(1, 361)
            #Array[16] contient des chiffres random ATTENTION
            ColonneS = []

            array[4][0] = montant_emprunt

            if per < 1 or per > Nombre_de_periodes:
                  raise ValueError("La valeur de 'pér' doit être comprise entre 1 et 'Nombre_de_periodes'.")
            #Colonne E et G 
            for i in range(1,Nombre_de_periodes + 1 ) : 
            
                  it = Nombre_de_periodes - i +  1
                  ppmt = -npf.ppmt(Periodical_basis, per, it, array[4][i - 1])
                  
                  array[5][i] = array[4][i - 1] * (1 + Periodical_basis) - array[4][i - 1]
                        
                  array[6][i] = ppmt 
                  array[7][i] = (array[4][i - 1] - array[6][i]) * Periodical_basis_2 

                  array[4][i] = array[4][i - 1] - array[6][i] - array[7][i]
                  #Colonne I 
                  for i in range(1,len(array[4])  ) : 
                        array[8][i] = array[5][i] + array[6][i] + array[7][i]

        
            #Colonne J 
            for i in range(1,len(array[9])) : 
                  if (nombre_de_payment_par_an == 1 ) : 
                        array[9][i] = i*array[8][i]
                  else : 
                        if(nombre_de_payment_par_an == 2 ) : 
                              array[9][i] = array[8][i]*array[1][i]
                        else : 
                              if(nombre_de_payment_par_an == 4) : 
                                    array[9][i] = array[8][i]*array[2][i]
                              else : 
                                    array[9][i] = array[8][i]*array[3][i]      
                              


            #Colonne K 
            for i in range(1,len(array[10])) : 
                  Exposant = 0 
                  if (nombre_de_payment_par_an == 1) : 
                        Exposant = i
                  else : 
                        if(nombre_de_payment_par_an == 2) : 
                              Exposant = array[1][i]
                        else : 
                              if(nombre_de_payment_par_an == 4) : 
                                    Exposant = array[2][i]
                              else : 
                                    Exposant = array[3][i]            
                  array[10][i] = array[8][i] / ( 1 + taux_interet_annuel)**Exposant
            
            #Colonne L 
            for i in range(1,len(array[10])) : 
                  Exposant = 0 
                  if (nombre_de_payment_par_an == 1) : 
                        Exposant = i
                  else : 
                        if(nombre_de_payment_par_an == 2) : 
                              Exposant = array[1][i]
                        else : 
                              if(nombre_de_payment_par_an == 4) : 
                                    Exposant = array[2][i]
                              else : 
                                    Exposant = array[3][i]            
                  array[11][i] = array[9][i] / ( 1 + taux_interet_annuel)**Exposant 

            array[14][0] = array[4][0] + array[7][0]
            #Colonne O et P 
            for i in range(1,Nombre_de_periodes + 1 ) : 
                  it = Nombre_de_periodes - i +  1
                  ppmt = -npf.ppmt(Periodical_basis, per, it, array[14][i - 1])
                  
                  array[12][i] = array[14][i - 1] * (1 + Periodical_basis) - array[14][i - 1]
                        
                  array[13][i] = ppmt 

                  array[14][i] = array[14][i - 1] - array[13][i] 
            
        


            #Colonne S T U  
            counter = 1
            while(array[3][counter] < Duree_repracing_anne and counter) : 
                  ColonneS.append(array[6][counter] + array[7][counter])
                  counter += 1
                  if (counter == 361) : 
                        break 
            ColonneS.append(0)  
            for i in range(len(ColonneS) , 361) : 
                  ColonneS.append(0)
            ColonneS = np.array(ColonneS)
            ColonneT = np.random.rand(len(ColonneS))


            for i in range(0,len(ColonneS)) : 
                  if (ColonneS[i] == 0 and ColonneS[i-1] > 0  ) : 
                        sum = 0 
                        for j in range(i+1,len(array[6])) : 
                              sum += array[6][j] + array[7][j] 
                        ColonneT[i] = sum      
                  else : 
                        ColonneT[i] = ColonneS[i]       






     







            

            # Sélectionner le sous-ensemble de lignes et de colonnes


            # Afficher les premières lignes du DataFrame pour vérification
            #print(data.head())

            # Accéder aux valeurs de la colonne E
            # ou data['Unnamed: 4'] si le nom de la colonne n'est pas 'E'
            lignes_5_7_col_E = data.iloc[7:25, 4]
            lignes_5_7_col_E = lignes_5_7_col_E.values
            # Pour inclure uniquement la colonne E
            # Afficher les valeurs de la colonne E

 





            def localspline(x, periodcol, ratecol):
                  period_count = len(periodcol)
                  rate_count = len(ratecol)
                  if period_count != rate_count:
                        return "Error: Range count does not match"
                  
                  xin = np.zeros(period_count)
                  yin = np.zeros(period_count)
                  for c in range(period_count):
                        xin[c] = periodcol[c]
                        yin[c] = ratecol[c]
                  
                  n = period_count
                  yt = np.zeros(n)
                  u = np.zeros(n-1)
                  yt[0] = 0
                  u[0] = 0
                  for i in range(1, n-1):
                        sig = (xin[i] - xin[i-1]) / (xin[i+1] - xin[i-1])
                        p = sig * yt[i-1] + 2
                        yt[i] = (sig - 1) / p
                        u[i] = (yin[i+1] - yin[i]) / (xin[i+1] - xin[i]) - (yin[i] - yin[i-1]) / (xin[i] - xin[i-1])
                        u[i] = (6 * u[i] / (xin[i+1] - xin[i-1]) - sig * u[i-1]) / p
                  
                  qn = 0
                  un = 0
                  yt[-1] = (un - qn * u[-2]) / (qn * yt[-2] + 1)
                  for k in range(n-2, -1, -1):
                        yt[k] = yt[k] * yt[k+1] + u[k]
                  
                  klo = 0
                  khi = n-1
                  while khi - klo > 1:
                        k = (khi + klo) // 2
                        if xin[k] > x:
                              khi = k
                        else:
                              klo = k
                  
                  h = xin[khi] - xin[klo]
                  a = (xin[khi] - x) / h
                  b = (x - xin[klo]) / h
                  y = a * yin[klo] + b * yin[khi] + ((a**3 - a) * yt[klo] + (b**3 - b) * yt[khi]) * (h**2) / 6
                  return y



            def local_interp(x_val, x_range, y_range, is_sorted=True):
                  if is_sorted:
                        # binary search sorted range
                        low = 0
                        high = len(x_range) - 1
                        while abs(high - low) > 1:
                              med = (low + high) // 2
                              if x_range[med] < x_val:
                                    low = med
                              else:
                                    high = med
                  else:
                        # search every entry
                        x_below = -1e+205
                        x_above = 1e+205
                        for med in range(len(x_range)):
                              test_val = x_range[med]
                              if test_val < x_val:
                                    if abs(x_val - test_val) < abs(x_val - x_below):
                                          low = med
                                          x_below = test_val
                              else:
                                    if abs(x_val - test_val) < abs(x_val - x_above):
                                          high = med
                                          x_above = test_val

                  x_below = x_range[low]
                  x_above = x_range[high]
                  y_below = y_range[low]
                  y_above = y_range[high]
                  return y_below + (x_val - x_below) * (y_above - y_below) / (x_above - x_below)



            lignes_5_7_col_E = data.iloc[7:25, 4].values
            G_base = data.iloc[7:25, 6 ].values


            #Colonne U
            ColonneU = np.zeros(len(ColonneT))
            for i in range(len(ColonneT)) : 
                  sum= 0 
                  for j in range(i,len(ColonneT)) : 
                        sum += ColonneT[j] 
                  ColonneU[i] = sum  



            #Colonne V 
            lignes_5_7_col_E = data.iloc[7:25, 4]
            lignes_5_7_col_E = lignes_5_7_col_E.values
            ColonneV = np.random.rand(len(ColonneR))
            for i in range(1,len((ColonneV))) : 
                  ColonneV[i-1] = localspline(i,G_base,lignes_5_7_col_E)

            #print(ColonneV)

            #Colonne W (Dernier chiffre veut pas s'enlever)
            J_base = data.iloc[7:25, 9].values

            #for j in range(0,len(J_base)) : 
                  #if (J_base[j] < 0 ) : 
                  #J_base[j] =  J_base[j]


            ColonneW = np.random.rand(len(ColonneR))
            for i in range(1,len(ColonneW)) : 
                  ColonneW[i-1] = local_interp(i , G_base , J_base)
            ColonneW[len(ColonneW)-1] = local_interp(360 , G_base , J_base)
            #Colonne X (Dernier chiffre pas enlevable non pkus)
            ColonneX = np.random.rand(len(ColonneR))
            for i in range(len(ColonneX)) : 
                  ColonneX[i] = ((1+ColonneW[i]/100)**(1/12)-1)*1200
            #Colonne Y 
            ColonneY = np.zeros(len(ColonneT))
            ColonneX_bis = ColonneX[:len(ColonneT)]
            for i in range(len(ColonneT)) : 
                  try : 
                              if i  != 0  : 
                                    ColonneY[-i] =  ColonneT[-i] *(ColonneX_bis[-i+1]/100)/12 + ColonneY[-i+1]
                                    #print(ColonneT[-i])
                                    #print(ColonneX_bis[-i+1])
                                    #print( ColonneY[-i+1])
                              
                  except : 
                        continue
            ColonneY[0] =  ColonneT[0] *(ColonneX_bis[0]/100)/12 + ColonneY[1]
                  
     
            #ColonneZ 
            ColonneZ = np.zeros(361)
            for i in range(len(ColonneZ)) : 
                  if(ColonneU[i] !=0) : 
                              ColonneZ[i] = ColonneY[i]*1200/ColonneU[i]

            #Interest FC 
            sum = 0 

            for i in range(360) : 
                  sum += ColonneY[i] * ColonneV[i]
            FC =sum 
            #Amortizing swap 
            AS = 0 
            for i in range(360):
                  AS+= ColonneV[i] * ColonneU[i] 
            AS = FC/AS*1200
            
            ASFinale = ((1+AS/100/12)**12-1)*100
            #print(array[6])
            #print(array[7])
            
            return ASFinale



            
        

    # Méthodes pour effectuer les calculs

# Paramètres à modifier
# parametres = Parametres(
#     Nombre_de_periodes=300,
#     taux_interet_annuel=1.617/100,
#     Duree_repracing_anne=100,
# )


