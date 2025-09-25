PIN_KORREKT = "2580"
tentativa = 3

while tentativa > 0:
    pin = input("PIN: ")
    if pin == PIN_KORREKT:
        print("Hyrje e lejuar")
        break
    else:
        tentativa -= 1
        if tentativa == 0:
            print("Karta u bllokua")
        else:
            print("Gabim. Tentativa te mbetura:", tentativa)
