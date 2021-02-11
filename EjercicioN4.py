
print("Proyecto Bimestral")
print("Alejandra Paute")
print("EjercicioN4: Realice un algoritmo que genere una matriz con cada uno de los recorridos que se muestran a continuación.")

# Declaración e inicialización de variables

n = int()
tp = int()
n = 0

print("Ingrese el límite")
n = int(input())

tp = [[int() for ind0 in range(n)] for ind1 in range(n)]

for i in range(1,n+1):
	for j in range(1,i+1):
		if j==1 or j==i:
			tp[i-1][j-1] = 1
		else:
			tp[i-1][j-1] = tp[i-2][j-2]+tp[i-2][j-1]

espacio = 1

#Triángulo de pascal de forma invertida
print("Triángulo de pascal de forma invertida")

for i in range(n,0,-1):
	for k in range(1,espacio+1):
		print(" ", end="")
	for j in range(1,i+1):
		print(tp[i-1][j-1]," ", end="")
	print(" ")
	espacio = espacio+1

k = float()
a = float()
l = float()

a = [[int() for ind0 in range(n)] for ind1 in range(n)]

espacio = 1
k = 1

for i in range(n,0,-1):
	l = espacio
	for j in range(1,i+1):
		a[k-1][l-1] = tp[i-1][j-1]
		l = l+1
	espacio = espacio+1
	k = k+1

espacio = 1

#Triángulo de pascal de forma invertida en una matriz

print("Triángulo de pascal de forma invertida en una matriz")

for i in range(1,n+1):
	for k in range(1,espacio+1):
		print(" ", end="")
	for j in range(1,n+1):
		if a[i-1][j-1]!=0:
			print(a[i-1][j-1]," ", end="")
	espacio = espacio+1
	print(" ")

