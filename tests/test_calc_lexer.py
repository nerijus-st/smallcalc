from smallcalc import calc_lexer as clex
from smallcalc import tok as token


def test_get_tokens_understands_eof():
    l = clex.CalcLexer()

    l.load('')

    assert l.get_tokens() == [token.Token(clex.EOF)]


def test_get_token_understands_integers():
    l = clex.CalcLexer()

    l.load('3')

    assert l.get_token() == token.Token(clex.INTEGER, '3')


def test_get_tokens_understands_integers():
    l = clex.CalcLexer()

    l.load('3')

    assert l.get_tokens() == [
        token.Token(clex.INTEGER, '3'),
        token.Token(clex.EOL),
        token.Token(clex.EOF)
    ]


def test_get_tokens_understands_unspaced_sum_of_integers():
    l = clex.CalcLexer()

    l.load('3+5')

    assert l.get_tokens() == [
        token.Token(clex.INTEGER, '3'),
        token.Token(clex.LITERAL, '+'),
        token.Token(clex.INTEGER, '5'),
        token.Token(clex.EOL),
        token.Token(clex.EOF)
    ]
