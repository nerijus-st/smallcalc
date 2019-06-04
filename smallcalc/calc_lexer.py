from smallcalc.tok import Token

EOF = 'EOF'
EOL = 'EOL'
INTEGER = 'INTEGER'

class CalcLexer:

    def load(self, some_value):
        self.value = some_value

    def get_token(self):
        token = Token(_type=INTEGER, value=self.value)
        return token

    def get_tokens(self):
        value_token = self.get_token()
        eol_token = Token(_type=EOL, value=None)
        eof_token = Token(_type=EOF, value=None)
        return [value_token, eol_token, eof_token]
