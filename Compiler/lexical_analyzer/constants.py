import string

# CONSTANTS
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = DIGITS+LETTERS

# TOKENTYPE(TT) CONSTANTS
TT_INT = 'int'
TT_FLOAT = 'float'
TT_PLUS = '+'
TT_MINUS = '-'
TT_MUL = '*'
TT_DIV = '/'
TT_LPAREN = '('
TT_RPAREN = ')'
TT_EOF = 'EOF'
TT_POW = '^'
TT_KEYWORD = 'KEYWORD'
TT_EQ = '='
TT_IDENTIFIER = 'IDENTIFIER'
TT_EE = '=='
TT_NE = '!='
TT_LT = '<'
TT_GT = '>'
TT_LTE = '<='
TT_GTE = '>='

KEYWORDS = [
    "VAR",
    "OR",
    "NOT",
    "AND"
]