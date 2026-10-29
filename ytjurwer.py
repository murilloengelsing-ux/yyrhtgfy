
def calculadora():
    print("=== CALCULADORA SIMPLES ===")

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")

        operacao = input("Digite o número da operação: ")

        if operacao == "1":
            resultado = numero1 + numero2
        elif operacao == "2":
            resultado = numero1 - numero2
        elif operacao == "3":
            resultado = numero1 * numero2
        elif operacao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                return
            resultado = numero1 / numero2
        else:
            print("Operação inválida!")
            return

        print(f"\nResultado: {resultado}")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")


if __name__ == "__main__":
    calculadora()

