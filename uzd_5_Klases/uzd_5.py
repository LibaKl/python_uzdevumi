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
        self.dzimums = dzimums
    

    
#funkcija atgriež info par dzīvnieku
    def info(self):
        return f"Vārds: {self.vards}, Vecums: {self.vecums} gadi, {self.dzimums}"


#apakšklase
class Trusis(Dzivnieks):
    def __init__(self, vards, vecums, dzimums, suga):
        super().__init__(vards, vecums, dzimums)
        self.suga = suga    
#funkcija atgriež info no Dzīvnieks + sugu
    def trusis_info(self):
        return f"{self.info()}, Suga: {self.suga}" 

mans_trusis1 = Trusis("Žožo", 3, Dzimums.Vīrietis, "Auntrusis")
mans_trusis2 = Trusis("Ūsiņš", 2, Dzimums.Vīrietis, "Liesmojošais trusis")

print("Dzīvnieku informācija:")
print(mans_trusis1.trusis_info())
print(mans_trusis2.info())