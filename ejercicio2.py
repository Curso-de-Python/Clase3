'''
-----------------------------
 EJERCICIO N°2
 Declaraciones condicionales
-----------------------------
 Aquí encontrarás 3 programas que resuelven el mismo problema: encuentran el número mayor y lo imprimen
-----------------------------
'''
# EJEMPLO 1 

# lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1> numero2:
  nmasGrande = numero1
else:
  nmasGrande = numero2

# imprimir el resultado
print("El número más grande es:", nmasGrande)

'''
# -----------------------------
# EJEMPLO 2: ¿Sabías que si alguna de las ramas if-elif-else contiene una sola instrucción, no necesitas escribirla en una nueva línea con sangría? Cambia la rama if-else por lo siguiente

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

# -----------------------------
# EJEMPLO 3: ¿Y si comparamos tres números?

# lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

# asumimos temporalmente que el primer número
# es el más grande,
# lo verificaremos pronto
nmasGrande = numero1

# comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

# comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
  nmasGrande = numero3

# imprimir el resultado
print("El número más grande es:", nmasGrande)
'''
