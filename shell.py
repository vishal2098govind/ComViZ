from Compiler.run import run

while True:
    text = input('comviz >')
    tokens, abstract_syntax_tree, error = run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print("Lexer Output: Tokens")
        print(tokens)
        print("Parser Output: Abstract Syntax Tree")
        print(abstract_syntax_tree)
