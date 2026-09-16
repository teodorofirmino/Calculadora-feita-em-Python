try:
    x = int(input("Bem vindo a sua calculadora feita em Python!\nDigite:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Radiciação\n7 - Sair\n"))
    if x == 1:
        y = float(input("Quais números você quer adicionar? Digite o primeiro número:\n"))
        z = float(input("Digite o segundo número\n"))
        print(y, "+", z, "=", y+z)
    elif x == 2:
        y = float(input("Quais números você quer subtrair? Digite o primeiro número:\n"))
        z = float(input("Digite o segundo número:\n"))
        print(y, "-", z, "=", y-z)
    elif x == 3:
        y = float(input("Quais números você quer multiplicar? Digite o primeiro número:\n"))
        z = float(input("Digite o segundo número:\n"))
        print(y, "×", z, "=", y*z)
    elif x == 4:
        y = float(input("Quais números você quer dividir? Digite o primeiro número:\n"))
        z = float(input("Digite o segundo número:\n"))
        print(y, "÷", z, "=", y/z)
    elif x == 5:
        y = float(input("Quais números você quer multiplicar por potência? Digite o primeiro número:\n"))
        z = float(input("Digite o segundo número:\n"))
        print(y, "^", z, "=", y**z)
    elif x == 6:
        y = float(input("Qual número você quer ter a raiz dele? Digite os números abaixo:\n"))
        z = float(input("Digite o radicando (número que fica de fora da raiz):\n"))
        print(z, "√", y, "=", y ** (1 / z))
    elif x == 7:
        print(:"Saindo...")
    elif x > 7:
        print("Digite apenas algum dos números acima para selecionar uma opção\n")
except ValueError:
    print("Apenas números são válidos.")