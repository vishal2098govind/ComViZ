from anytree import AnyNode
from Compiler.run import run
from Visualiser.visualise_ast import visualize_ast
from Visualiser.visualise_pt import visualize_parse_tree

while True:
    text = input('comviz >')
    visualize_parse_tree(None)
    visualize_ast()
    tokens, abstract_syntax_tree_root, any_error, runtime_result = run('<stdin>', text)

    if any_error:
        print(any_error.as_string())
    else:
        print("Lexer Output: Tokens")
        print(tokens)
        print("Parser Output: Abstract Syntax Tree")
        print(abstract_syntax_tree_root)
        if runtime_result:
            print('Interpreter Output: Result')
            print(runtime_result)
            # visualize_ast(node=abstract_syntax_tree_root)
