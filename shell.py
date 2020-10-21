from Compiler.lexical_analysis.Lexer import Lexer

while True:
    standard_input = '234+&'
    text = input('comviz >')
    lexer = Lexer(text)
    result, error = lexer.make_token
    if error:
        print(error.as_string())
    else:
        print(result)
