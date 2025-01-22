from enum import Enum

class Dzimums(Enum):
    Nav_norādīts = 0
    Vīrietis = 1
    Sieviete = 2
    

#virsklase Dzīvnieks
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


#apakšklase
class Trusis(Dzivnieks):
    def __init__(self, vards, vecums, dzimums, suga):
        super().__init__(vards, vecums, dzimums)
        self.suga = suga    
#funkcija atgriež info no Dzīvnieks + sugu
    def trusis_info(self):
        try:
            return f"{self.info()}, Suga: {self.suga}" 
        except:
            print("Exception")


def dzivnieka_generesana(vards, vecums, dzimums, suga):
    try:
        return Trusis(vards, vecums, dzimums, suga)
    except ValueError:
        print("Dzimums ir jābūt no Dzimums Enum klases.")

      
#pareizi atzīmēta enum vērtība - dzimums
mans_trusis1 = dzivnieka_generesana("Žožo", 3, Dzimums.Vīrietis, "Auntrusis")
mans_trusis2 = dzivnieka_generesana("Ūsiņš", 2, Dzimums.Vīrietis, "Liesmojošais trusis")
#nepareizi atzīmēta enum vērtība - dzimums
mans_trusis3 = dzivnieka_generesana("Ūsiņš", 2, "Vīrietis", "Liesmojošais trusis")

print("Dzīvnieku informācija:")
print(mans_trusis1.trusis_info())
print(mans_trusis2.trusis_info())
#izmet kļūdu jo nepareizs dzimums, bet parāda sugu, jo izmanto trusis_info() funkciju
print(mans_trusis3.trusis_info())