#saraksts
dzivnieku_saraksts = ["Trusis", "Kaķis", "Suns", "Papagailis"]
#pievieno sarakstam
dzivnieku_saraksts.append("Zivtiņa")
#noņem no saraksta
dzivnieku_saraksts.remove("Suns")
#vienkārša funkcija ar sarakstu
for dzivnieks in dzivnieku_saraksts:
    print(f"Man patīk šādi dzīvnieki: {dzivnieks}")

#vārdnīca
dzivnieka_info = {
    "vards": "Žožo",
    "vecums" :3,
    "dzimums":"Vīrietis"
}
# Iegūst dzīvnieka vārdu
print("Dzīvnieka vārds:")
vards = dzivnieka_info.get("vards")
print(vards)
# Nomaina dzīvnieka vecumu
dzivnieka_info["vecums"] = 6
print("Atjaunināta dzīvnieka informācija:")
print(dzivnieka_info)


#set-ja atkartojas, to neizdrukās
dazadi_dzivnieki = {"Trusis", "Trusis", "Pūķis", "Kaķis"}
print(dazadi_dzivnieki)
#pievieno
dazadi_dzivnieki.add("Suns")
#noņem
dazadi_dzivnieki.remove("Pūķis")
print(dazadi_dzivnieki)

#Tuple
dzivnieku_vardi = ("Žožo", "Ūsiņš", "Pūķis","Ūsiņš")
print(dzivnieku_vardi)
#apskata konkrētu indeksu
print("Otrā dzīvnieka vārds:")
print(dzivnieku_vardi[1])
#darbības ar tuple
varda_skaits = dzivnieku_vardi.count("Ūsiņš")
print(f"'Ūsiņš' tuple parādās {varda_skaits} reizes.")
