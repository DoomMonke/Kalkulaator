#Alari Viilma
#03.01.2023
#Euro-Krooni kalkulaator

#1 Euro hind Kroonides ja 1 Krooni hind Eurodes
Euro_Kroonidesse= 15.6466
Kroonid_Eurodesse= 0.0641

#Küsib inimeselt mida ta soovib kalkuleerida
kalkuleerida = input("Kas soovite kalkuleerida Eurodest Kroonidesse või Kroonidest Eurodesse? (E/e Euro>Kroonidesse, K/k Kroonid > Eurodesse): ")

#Uurib kas inimene pani õige vastuse
if kalkuleerida == "E" or kalkuleerida == "e":
    #kalkuleerib kui palju Eurot on võrdne Krooniga
    summa = float(input("Sisesta euro summa: "))
    tulemus = summa * Euro_Kroonidesse
    print (f"{summa} Euro(t) on võrdne {tulemus} Krooniga.")
if kalkuleerida == "K" or kalkuleerida == "k":
    #kalkuleerib kui palju Krooni on võrdne Euroga
    summa = float(input("Sisesta Krooni summa: "))
    tulemus = summa * Euro_Kroonidesse
    print (f"{summa} Kroon(i) on võrdne {tulemus} Euroga.")
#kui inimene paneb vale tähe
else:
    print("Vabandust, see ei olnud õige tähemärk, Palun proovige uuesti")