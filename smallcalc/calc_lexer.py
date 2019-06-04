from smallcalc.tok import Token

EOF = 'EOF'


class CalcLexer:

    def load(self, some_value):
        self.value = some_value

    def get_tokens(self):
        token = Token(_type=EOF, value=None)
        return [token]
