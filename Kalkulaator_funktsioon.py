def kalkulaator(valik, summa):
    eur_to_EEK = 15.6466
    EEK_to_eur = 0.064
    if valik == "EUR>EEK":
        result = summa * eur_to_EEK
    elif valik == "EEK>EUR":
        result = summa * EEK_to_eur
    else:
        return "Error: Vale valik. Valige kas 'EUR>EEK' või 'EEK>EUR'"
    return result

valik = input("Palun valige kas tahate Euro Kroondise või Kroonid Eurodesse (EUR>EEK või EEK>EUR): ")
summa = float(input("Palun sisestage summa: "))

print("Result: ", kalkulaator(valik, summa))