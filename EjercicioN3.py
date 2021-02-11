
print("Proyecto Bimestral")
print("Alejandra Paute")
print("EjercicioN3: Construir una función que reciba como parámetros una matriz 4x4 entera y un valor entero y retorne la cantidad de veces que se repite dicho valor en la matriz.")

# Funcion 

def numeroo(a, n, nume):
	cont = int()
	cont = 0
	for i in range(1,n+1):
		for j in range(1,n+1):
			if a[i-1][j-1]==nume:
				cont = cont+1

	print("Las veces que el número ",nume," se repitio en la matriz es ",cont," veces")

# Metodo principal

# Declaración de variables

n = int()
nume = int()
a = int()
n = 4
nume = 0

# Arreglo

a = [[int() for ind0 in range(6)] for ind1 in range(4)]

# Llenar matriz A

print("Ingrese los valores de la matriz")

for i in range(1,n+1):
	for j in range(1,n+1):
		print("A[",i,"][",j,"]")
		a[i-1][j-1] = int(input())

# Presentacion del arreglo A 

print("Arreglo Actual")

for i in range(1,n+1):
	for j in range(1,n+1):
		print(a[i-1][j-1],"  ", end="")
	print(" ")

print("Ingrese el número a verificar las veces que se repite")

nume = int(input())

numeroo(a,n,nume)

