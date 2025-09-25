while True:
    print("\nMenu:")
    print("1) Pershendetje")
    print("2) Shume e dy numrave")
    print("3) Ndihme")
    print("0) Dalje")

    zgjedhja = input("Zgjedhja: ").strip()

    if zgjedhja == '1':
        print("Përshëndetje!")
        continue
    elif zgjedhja == '2':
        a = float(input("Jep a: "))
        b = float(input("Jep b: "))
        print("Shuma:", a + b)
        continue
    elif zgjedhja == '3':
        print("Zgjedh 1 për përshëndetje, 2 për shumën, 3 për ndihmë, 0 për dalje.")
        continue
    elif zgjedhja == '0':
        print("Dalje nga programi.")
        break
    else:
        print("Zgjedhje e pavlefshme.")
        continue
