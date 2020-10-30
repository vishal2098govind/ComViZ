from anytree import AnyNode
from anytree.exporter import UniqueDotExporter

from Compiler.run import run
from Visualiser.visualise_ast import visualize_ast
from Visualiser.visualise_pt import visualize_parse_tree
# from Visualiser.visualise_st import visualise_st

UniqueDotExporter(AnyNode(name='')).to_picture("arith_ast.png")
while True:
    text = input('comviz >')
    UniqueDotExporter(AnyNode(name='')).to_picture("arith_ast.png")
    visualize_parse_tree(None)
    visualize_ast()
    tokens, ast_trace, any_error, runtime_result = run('<stdin>', text)

    if any_error:
        print(any_error.as_string())
    else:
        # print("Lexer Output: Tokens")
        print(tokens)
        # print("Parser Output: Abstract Syntax Tree")
        visualize_parse_tree(ast_trace[1])
        # print(ast_trace[0])
        if runtime_result:
            # print('Interpreter Output: Result')
            print(runtime_result)
            # if not isinstance(ast_trace[0], IfNode):
            #     re_trace = visualize_ast(node=ast_trace[0])
            #     for pre, fill, node in RenderTree(re_trace[0]):
            #         print(f'{pre}{node.name}')
            #     trace.clear()
            # visualise_st()
