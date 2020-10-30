import string

# CONSTANTS
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = DIGITS+LETTERS

# TOKENTYPE(TT) CONSTANTS
TT_INT = 'int'
TT_FLOAT = 'float'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = '('
TT_RPAREN = ')'
TT_EOF = 'EOF'
TT_POW = 'POW'
TT_KEYWORD = 'KEYWORD'
TT_EQ = 'EQ'
TT_IDENTIFIER = 'ID'
TT_EE = 'EE'
TT_NE = 'NE'
TT_LT = 'LT'
TT_GT = 'GT'
TT_LTE = 'LTE'
TT_GTE = 'GTE'

KEYWORDS = [
    "VAR",
    "OR",
    "NOT",
    "AND",
    "IF",
    "THEN",
    "ELSE",
    "ELIF",
]
