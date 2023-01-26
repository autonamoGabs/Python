e = ""
g = ""
entrada = input("Frase: ")
frase = entrada.replace(" ","")
b = len(frase)
for c in range(0,b):
  d = frase[c]
  e = e + d
for i in range(b,0,-1):
  f = frase[i-1]
  g = g + f

if g == e:
  print("é polindromo")
else:
  print("não é")