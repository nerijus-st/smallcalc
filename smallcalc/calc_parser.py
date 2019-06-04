from dataclasses import dataclass

from smallcalc.calc_lexer import CalcLexer, INTEGER


@dataclass
class IntegerNode:
    value: int

    def __init__(self, value):
        self.value = int(value)
        self.type = INTEGER

    def asdict(self):
        return {
            'type': self.type,
            'value': self.value
        }


class CalcParser:
    def __init__(self):
        self.lexer = CalcLexer()

    def parse_integer(self):
        return IntegerNode(self.lexer.value)
