from smallcalc.calc_parser import CalcParser


class CalcVisitor:
    def visit(self, ast):
        parser = CalcParser()
        parser.lexer.load(ast['value'])
        node = parser.parse_integer()
        return (node.value, node.type)
