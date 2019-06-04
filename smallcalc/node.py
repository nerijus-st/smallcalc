from dataclasses import dataclass


# from smallcalc.calc_lexer import INTEGER, LITERAL


@dataclass
class IntegerNode:
    value: int

    def __init__(self, value):
        self.value = int(value)
        self.type = 'integer'

    def asdict(self):
        return {
            'type': self.type,
            'value': self.value
        }


@dataclass
class LiteralNode:
    value: str

    def __init__(self, value):
        self.value = str(value)
        self.type = 'literal'

    def asdict(self):
        return {
            'type': self.type,
            'value': self.value
        }


class ExpressionNode:
    value: str

    def __init__(self, left, right, operator):
        self.type = 'binary'
        self.left = left
        self.right = right
        self.operator = operator

    def asdict(self):
        return {
            'type': self.type,
            'left': self.left.asdict(),
            'right': self.right.asdict(),
            'operator': self.operator.asdict()
        }
