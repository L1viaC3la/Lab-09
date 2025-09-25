count = 0
total = 0.0
min_val = None
max_val = None

while True:
    txt = input("Vlera: ").lower().strip()
    if txt == "stop":
        break
    try:
        num = float(txt)
        count += 1
        total += num
        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num
    except ValueError:
        print("Vlerë e pavlefshme")

print("-----------------")
if count == 0:
    print("Nuk u dhanë të dhëna.")
else:
    mesatare = total / count
    print(f"Count: {count}")
    print(f"Min: {round(min_val, 2)}")
    print(f"Max: {round(max_val, 2)}")
    print(f"Mesatare: {round(mesatare, 2)}")
