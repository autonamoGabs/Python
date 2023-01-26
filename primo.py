x = 0
z = int(input("Numero: "))
for c in range(2,z):
  if z % c == 0:
    x = x + 1
if z == 2:
    print("É primo")
elif x == 0:
  print("É primo")
else:
  print("não primo")

