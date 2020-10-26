from Compiler.run import run

while True:
    text = input('comviz >')
    tokens, abstract_syntax_tree, error, result = run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        if tokens and abstract_syntax_tree and error:
            print("Lexer Output: Tokens")
            print(tokens)
            print("Parser Output: Abstract Syntax Tree")
            print(abstract_syntax_tree)
        if result:
            print('Interpreter Output: Result')
            print(result)
