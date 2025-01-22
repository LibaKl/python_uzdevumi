from uzd_7.dzivnieks import Dzivnieks


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