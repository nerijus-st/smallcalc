import re

from smallcalc.tok import Token

EOF = 'EOF'
EOL = 'EOL'
INTEGER = 'integer'
LITERAL = 'literal'


class CalcLexer:

    def __init__(self):
        self.tokens = []
        self.ast = {}

    def load(self, value):
        if value:
            self.ast['type'] = 'single'
            left_pattern = r'\d+?(?=\D)'
            right_pattern = r'(?<=\D)\d+'
            operator_pattern = r'\D'
            if type(value) is str and len(value) > 1:
                self.ast['type'] = 'binary'

                left_value = re.search(left_pattern, value).group(0)
                token = Token(_type=INTEGER, value=left_value)
                self.tokens.append(token)
                self.ast['left'] = token

                operator_value = re.search(operator_pattern, value).group(0)
                token = Token(_type=LITERAL, value=operator_value)
                self.tokens.append(token)
                self.ast['operator'] = token

                right_value = re.search(right_pattern, value).group(0)
                token = Token(_type=INTEGER, value=right_value)
                self.tokens.append(token)
                self.ast['right'] = token
            else:
                self.tokens.append(Token(_type=INTEGER, value=value))
            self.tokens.append(Token(_type=EOL, value=None))
        self.tokens.append(Token(_type=EOF, value=None))

    def get_token(self):
        return self.tokens[0]

    def get_tokens(self):
        return self.tokens
