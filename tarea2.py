#Hallar el segundo mayor, el mayor y el menor

a1 = int(input("Ingrese el primer numero: "))
b2 = int(input("Ingrese el segundo numero: "))
c3 = int(input("Ingrese el tercero numero: "))
d4 = int(input("Ingrese el cuarto numero: "))
e5 = int(input("Ingrese el quinto numero: "))

numeros = [a1, b2, c3, d4, e5]

maximo = max(numeros)
numeros.remove(maximo)  

segundo_max = max(numeros)

print("El número mayor es:", maximo)
print("El número menor es:", min(numeros))
print("El segundo número más grande es:", segundo_max)