
print("=== Calculadora ===")
n1 = float(input("numero: "))
n2 = float(input("numero: "))
o = input("Operacion +-*/: ")
print("Resultado:", c(n1, n2, o))
def c(num_1, num_2, operacion):
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