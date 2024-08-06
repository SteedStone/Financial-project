import pandas as pd
import numpy as np 
import numpy_financial as npf
import Appli_copy as app 
import unittest



# Creation des paramètre nécessaire aux tests 

File_path = 'Calcul Hedging_Rates_BBG_based_NEW_INCL_SECUR_Factor_V2.2_frozen.xlsm'
file_class = app.GestionFichier(File_path)



# Serie de test pour la fonction de calcul de la valeur actuelle nette

class TestAppli_copy(unittest.TestCase):
    # Test Mortgage20Y_111 = 0,512
    def test_right_return_value0(self):
        parametres0 = app.Parametres(
            Nombre_de_periodes=240,
            taux_interet_annuel=1.42/100,
            Duree_repracing_anne=1,
        )
        calculs = app.Calculs(parametres0, file_class)
        self.assertEqual(round(calculs.retourne_valeurs_attendue(),3), -0.512)

    def test_right_return_value1(self):
        parametres0 = app.Parametres(
            Nombre_de_periodes=216,
            taux_interet_annuel=1.216/100,
            Duree_repracing_anne=100,
        )
        calculs = app.Calculs(parametres0, file_class)
        self.assertEqual(round(calculs.retourne_valeurs_attendue(),3), -0.192)

if __name__ == '__main__':
    unittest.main()