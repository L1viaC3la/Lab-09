n = int(input("Jep n: "))
shuma = 0
faktoriel = 1

for i in range(1, n + 1):
    shuma += i
    faktoriel *= i

print("Shuma 1..n:", shuma)
print("Faktorieli i n:", faktoriel if n > 0 else 1)
