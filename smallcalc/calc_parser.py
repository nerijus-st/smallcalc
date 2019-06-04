from smallcalc.calc_lexer import CalcLexer
from smallcalc.node import IntegerNode, LiteralNode, ExpressionNode


class CalcParser:
    def __init__(self):
        self.lexer = CalcLexer()

    def parse_integer(self):
        for token in self.lexer.tokens:
            print('123123', token.type)
            if token.type == 'integer':
                integer_token = self.lexer.tokens.pop(0)
                return IntegerNode(integer_token.value)
            elif token.type == 'literal':
                return self.parse_literal()

    def parse_literal(self):
        for token in self.lexer.tokens:
            if token.type == 'literal':
                literal_token = self.lexer.tokens.pop(0)
                return LiteralNode(literal_token.value)
            elif token.type == 'integer':
                return self.parse_integer()

    def parse_expression(self):
        left = self.parse_integer()
        operator = self.parse_literal()
        right = self.parse_integer()

        node = ExpressionNode(left, right, operator)

        return node
