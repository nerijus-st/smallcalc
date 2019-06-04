from smallcalc.calc_parser import CalcParser


class CalcVisitor:

    def __init__(self):
        self.parser = CalcParser()

    def visit(self, ast):
        if ast['type'] != 'binary':
            self.parser.lexer.load(ast['value'])
            node = self.parser.parse_integer()
            self.parser.lexer.tokens = []
            self.parser.lexer.ast = []
            return (node.value, node.type)
        elif ast['type'] == 'binary':
            _expression = []
            _expression.append(ast['left']['value'])
            _expression.append(ast['operator']['value'])
            _expression.append(ast['right']['value'])
            self.parser.lexer.load("".join(map(str, _expression)))
            node = self.parser.parse_expression()
            self.parser.lexer.tokens = []
            self.parser.lexer.ast = {}
            return self._calculate(node)

    def _calculate(self, node):
        if node.operator.value == '+':
            value = node.left.value + node.right.value
            return (value, 'integer')
