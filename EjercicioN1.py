
print("Proyecto Bimestral")
print("Alejandra Paute")
print("EjercicioN1:Leer n números enteros, almacenarlos en un vector y determinar a ¿Cuánto es igual la suma de los dígitos pares de cada uno de los números leídos?.")

# Declaración de variables

n = int()
suma = int()

# Inicialización de variables
n = 0
suma = 0

# Datos de entrada

print("Ingrese el límite del vector: ")
n = int(input())

# Declarar vector 

a = int()
a = [int() for ind0 in range(n)]

# Ingresando los datos del Arreglo A

print("Ingrese los datos del arreglo A: ")
for i in range(1,n+1):
	print("Ingrese el elemento A[",i,"]: ")
	a[i-1] = int(input())

# Suma de Pares

for i in range(1,n+1):
	if a[i-1]%2==0:
		suma = suma+a[i-1]
print("La suma de los números pares dentro del vector es: ",suma)

