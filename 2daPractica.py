nombre = input("Ingresa tu nombre: ")
print("Hola "+nombre)
print(f"Holaa {nombre}")
print("Holaaa {}".format(nombre))

edad = 25 #entero
altura = 1.74 #flotante
#convertir a flotante
edadString = str(edad)
bola = True

print(edad + edad)
print(edadString + edadString)

print(type(edad))

tuedad = input("Introduce tu edad: ")
tuedad = int(tuedad)

if tuedad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

for i in range(0, 10):
    print(i)

dia = input("Introduce un día: ")
dia = int(dia)

