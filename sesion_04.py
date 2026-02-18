# Instrucciones Función Calculadora:
# Cree un función en python llamada calculadora, la cual debe tomar los parámetros (num_1, num_2, operacion) y debe ser capaz de realizar toda la lógica de un calculadora simple como: sumar, restar, multiplicar y dividir.
# Nota: Las entradas serán proporcionadas por el usuario.
# Pista: Este código es un ejemplo de una suma 

#num_1 = float(input("Escriba el valor del primer numero: "))
#num_2 = float(input("Escriba el valor del segundo numero: "))
#operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

#ef suma(num_1, num_2):
#    return num_1 + num_2

#if operacion == "+":
#    resultado = suma(num_1, num_2)
#    print("El resultado de la suma es: ", resultado)

print("=== Calculadora ===")

num_1 = float(input("Primer numero: "))
num_2 = float(input("Segundo numero: "))
operacion = input("Operacion (+, -, *, /): ")

def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    if operacion == "-":
        return num_1 - num_2
    if operacion == "*":
        return num_1 * num_2
    if operacion == "/":
        if num_2 == 0:
            return "No se puede dividir entre 0"
        return num_1 / num_2
    return "Operacion no valida"

print("Resultado:", calculadora(num_1, num_2, operacion))