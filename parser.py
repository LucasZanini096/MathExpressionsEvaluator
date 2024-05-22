class Parser:
    def __init__(self):
        self.operators = []
        self.postfix = []

    def to_postfix_notation(self, expression):
        open_parentheses = 0
        close_parentheses = 0

        for token in expression:
            if token.isalpha():
                self.postfix.append(token)
                continue

            if self.is_operator(token):
                while self.operators and self.has_precedence(self.operators[-1], token):
                    self.postfix.append(self.operators.pop())
                self.operators.append(token)
                continue

            if token == '(':
                open_parentheses += 1
                self.operators.append(token)
                continue

            if token == ')':
                close_parentheses += 1
                while self.operators and self.operators[-1] != '(':
                    self.postfix.append(self.operators.pop())
                if not self.operators:
                    raise ValueError("Closing parenthesis without corresponding opening parenthesis.")
                self.operators.pop()
                continue

            raise ValueError("Invalid operator.")

        if open_parentheses != close_parentheses:
            raise ValueError("Incorrect number of parentheses.")

        if not self.postfix and expression.strip():
            raise ValueError("Invalid number of operands.")

        while self.operators:
            self.postfix.append(self.operators.pop())

        return ''.join(self.postfix)

    @staticmethod
    def has_precedence(operator1, operator2):
        priority1 = Parser.get_priority(operator1)
        priority2 = Parser.get_priority(operator2)
        return priority1 >= priority2

    @staticmethod
    def get_priority(operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

    @staticmethod
    def is_operator(token):
        return token in "+-*/^"
