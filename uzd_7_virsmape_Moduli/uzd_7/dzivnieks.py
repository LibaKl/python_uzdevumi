
from uzd_7.dzimums import Dzimums 


class Dzivnieks:
    def __init__(self, vards, vecums, dzimums):
        self.vards = vards
        self.vecums = vecums
        if isinstance(dzimums, Dzimums):  # Pārbaudām, vai dzimums ir Enum vērtība
            self.dzimums = dzimums
        else:
            return ValueError("Dzimums ir jābūt no Dzimums Enum klases.")
        
        #funkcija atgriež info par dzīvnieku
    def info(self):
        try:
            return f"Vārds: {self.vards}, Vecums: {self.vecums} gadi, {self.dzimums}"
        except:
            print("Exception-dzimums")
