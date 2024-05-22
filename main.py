from evaluator import Evaluator
from parser import Parser

def main():
    values = []

    arithmetic_expression = ""
    postfix_expression = ""

    parser = Parser()
    evaluator = Evaluator()

    while True:
        try:
            print("""
                1. Entrada da expressão aritmética na notação infixa.
                2. Entrada dos valores numéricos associados às variáveis.
                3. Conversão da expressão, da notação infixa para a notação posfixa, e exibição da expressão
                convertida para posfixa.
                4. Avaliação da expressão (apresentação do resultado do cálculo, mostrando a expressão e os
                valores das variáveis).
                5. Encerramento do programa.
                """)

            choice = input("Digite uma das opções apresentadas: ").strip()

            if choice == '1':
                arithmetic_expression = input("Digite uma expressão aritmética de notação infixa: ").strip()

            elif choice == '2':
                if not arithmetic_expression:
                    print("Não foi digitada uma expressão de notação infixa!\nVoltando para o menu...")
                    continue

                for c in arithmetic_expression:
                    if not c.isalpha():
                        continue

                    value = float(input(f"Digite um valor para a variável {c}: "))
                    values.append(value)

            elif choice == '3':
                if not arithmetic_expression:
                    print("Não foi digitada uma expressão de notação infixa!\nVoltando para o menu...")
                    continue

                postfix_expression = parser.to_postfix_notation(arithmetic_expression)
                print(postfix_expression)

            elif choice == '4':
                if not postfix_expression:
                    print("Não existe uma expressão de notação posfixa!\nVoltando para o menu...")
                    continue

                values_in = values[:]
                result = evaluator.evaluate(postfix_expression, values_in)

                print("A expressão posfixa é:", postfix_expression)

                count = 0
                for c in arithmetic_expression:
                    if c.isalpha():
                        print(f"Variável {c} possui valor {values_in[count]}.")
                        count += 1

                print("O resultado da expressão é", result)

            elif choice == '5':
                print("Finalizando o programa....")
                break

            else:
                print("Você não digitou uma das opções apresentadas.\nDigite novamente uma nova opção")

        except ValueError:
            print("Você deve digitar uma opção válida.\nVoltando para o menu....")

        except Exception as e:
            print("Uma erro inesperado acontenceu.", str(e))

if __name__ == "__main__":
    main()