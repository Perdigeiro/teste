operacao = input("Digite a operação: ")

if operacao == "+":

    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    print(f'{valor1} + {valor2} = {valor1 + valor2}')

elif operacao == "-":

    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    print(f'{valor1} - {valor2} = {valor1 - valor2}')

elif operacao == "*":

    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    print(f'{valor1} * {valor2} = {valor1 * valor2}')

elif operacao == "/":

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    print(f'{valor1} / {valor2} = {valor1 / valor2}')

else:
    print("fim...")

contador = 1
while contador < 5:
    print("Contador:", contador)
    contador += 1

for i in range(5):
    print("i:", i) 
    