class Evaluator:

    def __init__(self):
        self.variables = []

    def evaluate(self, postfix_expression, values):
        for token in postfix_expression:
            if token.isalpha():
                variable_index = ord(token) - ord('A')
                variable_value = values[variable_index]
                self.variables.append(variable_value)
                continue

            if self.is_operator(token):
                operand2 = self.variables.pop()
                operand1 = self.variables.pop()
                result = self.apply(token, operand1, operand2)
                self.variables.append(result)

        return self.variables.pop()

    def apply(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ArithmeticException("Operação inválida. Divisão por 0.")
            return operand1 / operand2
        elif operator == '^':
            return operand1 ** operand2
        else:
            raise ValueError(f"Unexpected value: {operator}")

    @staticmethod
    def is_operator(token):
        return token in "+-*/^"
