from uzd_7.dzimums import Dzimums
from uzd_7.trusis import Trusis


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