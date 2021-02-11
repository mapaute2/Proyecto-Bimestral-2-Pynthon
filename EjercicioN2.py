
print("Proyecto Bimestral")
print("Alejandra Paute")
print("EjercicioN2: Leer dos matrices 4x6 enteras y determinar cuál es el mayor dato almacenado en ella que pertenezca a la serie de Fibonacci.")

# Declaración e inicialización de variables

mayorr = int()
mayorr1 = int()
a = int()
b =int()
fibo = int()
mayorr = 0
mayorr1 = 0

a = [[int() for ind0 in range(6)] for ind1 in range(4)]
b = [[int() for ind0 in range(6)] for ind1 in range(4)]

# Llenar matriz A

print("Ingrese los valores de la matriz")
for i in range(1,5):
	for j in range(1,7):
		print("A[",i,"][",j,"]")
		a[i-1][j-1] = int(input())

# Presentacion del arreglo A

print("Arreglo Actual")
for i in range(1,5):
	for j in range(1,7):
		print(a[i-1][j-1],"  ", end="")
	print(" ")

# Llenar matriz B

print("Ingrese los valores de la matriz")
for i in range(1,5):
	for j in range(1,7):
		print("B[",i,"][",j,"]")
		b[i-1][j-1] = int(input())

# Presentacion del arreglo B

print("Arreglo Actual")
for i in range(1,5):
	for j in range(1,7):
		print(b[i-1][j-1],"  ", end="")
	print(" ")

# Valor mayor A 

mayorr = a[0][0]
for i in range(1,5):
	for j in range(1,7):
		if a[i-1][j-1]>mayorr:
			mayorr = a[i-1][j-1]

i = int()
fiboo = int()
primero = int()
segundoo = int()

i = 0
fiboo = 0
primero = 0
segundoo = 1

while fiboo<=mayorr:
	fiboo = primero+segundoo
	primero = segundoo
	segundoo = fiboo
	i = i+1

primero = 0
segundoo = 1

c = [float() for ind0 in range(i)]

for j in range(1,i):
	c[j-1] = primero+segundoo
	primero = segundoo
	segundoo = c[j-1]

bandera = bool()
num = int()
bandera = False

for l in range(i-1,0,-1):
	for j in range(1,5):
		for k in range(1,7):
			if a[j-1][k-1]==c[l-1] and bandera==False:
				num = a[j-1][k-1]
				bandera = True

print("El número mayor de la matriz A que pertence a la serie Figonacci es: ",num)

# Valor mayor B

mayorr1 = b[0][0]

for i in range(1,5):
	for j in range(1,7):
		if b[i-1][j-1]>mayorr1:
			mayorr1 = b[i-1][j-1]

i = 0
fiboo = 0
primero = 0
segundoo = 1

while fiboo<=mayorr1:
	fiboo = primero+segundoo
	primero = segundoo
	segundoo = fiboo
	i = i+1

primero = 0
segundoo = 1

c1 = [float() for ind0 in range(i)]

for j in range(1,i):
	c1[j-1] = primero+segundoo
	primero = segundoo
	segundoo = c1[j-1]

nume = int()
bandera = False

for l in range(i-1,0,-1):
	for j in range(1,5):
		for k in range(1,7):
			if b[j-1][k-1]==c1[l-1] and bandera==False:
				nume = b[j-1][k-1]
				bandera = True
				
print("El número mayor de la matriz A que pertence a la serie Figonacci es: ",nume)

