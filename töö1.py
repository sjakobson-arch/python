
# 
# 1.1. Tsitaat
# Koostada programm, mis väljastab ekraanile järgmise lause täpselt sellisel kujul, koos jutumärkide ja kirjavahemärkidega:
#  Albert Einstein ütles: "Kujutlusvõime on tähtsam kui teadmine."
#  Vihje: mõtle, kuidas kirjutada jutumärgid sõne sisse nii, et programm neid õigesti kuvaks.

print('Albert Einstein ütles: "Kujutlusvõime on tähtsam kui teadmine."')

# 
# 1.2. Esimene sisepõlemismootoriga auto
#  Koostada programm, mille
# real luuakse muutuja aasta ja antakse sellele väärtuseks 1885 (arvuna);
# real luuakse muutuja auto ja antakse sellele väärtuseks "Benz Patent-Motorwagen" (sõnena);
# real luuakse muutuja lause_keskosa ja antakse sellele väärtuseks . aastal valmis esimene sisepõlemismootoriga auto nimega (sõnena);
# real luuakse muutuja lause, mille väärtuseks saadakse eelmised muutujad ühendades (vajadusel teisendades arvu sõneks);
# real väljastatakse muutuja lause väärtus ekraanile.


aasta = "1885"
auto = " Benz Patent-Motorwagen."
lause_keskosa = ". aastal valmis esimene sisepõlemismootoriga auto nimega"
lause = aasta + lause_keskosa + auto
print(lause)


# 1.3. Eksami tulemus
#  Koostada programm, mis
#  – küsib kasutajalt eksamitulemuse protsendina (näiteks 78.5),
#  – väljastab hinde järgmise jaotuse alusel:
#   90% või rohkem – hinne 5
#   75% kuni 89.99% – hinne 4
#   50% kuni 74.99% – hinne 3
#   alla 50% – hinne 2
# Näidisväljund:
#  Tulemus: 78.5% → hinne 4

tulemus = int(input("Sisesta tulemuse protsent: "))
if tulemus >=90:
    print(5)
elif tulemus >=75:
    print(4)
elif tulemus >=50:
    print(3)
else:
    print(2)



# 1.4. Lauad ja toolid
#  Klassis on teatud arv õpilasi ning igas lauas on 2 kohta.
#  Koostada programm, mis
#  – küsib õpilaste arvu,
#  – arvutab ja väljastab, mitu täis lauda on vaja ning mitu õpilast jääb ilma lauapartnerita.
# Vihje: kasuta tehteid // ja %.

#  Testi näiteks andmetega:
#  õpilasi 15
#  õpilasi 20
#  õpilasi 7


õpilase_arv = int(input("Õpilaste arv: "))
kohad_lauas = 2

täis_laud = õpilase_arv // kohad_lauas
lauapartnerita = õpilase_arv % kohad_lauas


print("Üksikute õpilaste arv:", lauapartnerita, ".Täislaude: ", täis_laud)










