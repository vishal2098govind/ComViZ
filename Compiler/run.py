from Compiler.lexical_analysis.Lexer import Lexer


def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_token()

    return tokens, error
