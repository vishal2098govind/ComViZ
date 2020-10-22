from Compiler.lexical_analyzer.lexer import Lexer
from Compiler.syntax_analyzer.parser import Parser


def run(file_name, text):
    """
    Args:
        file_name:
        text:

    Returns: ( tokens, abstract_syn_tree, error )
    """
    # Generate Tokens
    lexer = Lexer(file_name, text)
    tokens, lexical_error = lexer.make_token()

    if lexical_error:
        # if lexical_error, no abstract_syn_tree will be able to be formed thus return None for abstract_syn_tree
        return tokens, None, lexical_error

    # Parse tokens
    parser = Parser(token_list=tokens)

    # Generate Abstract Syntax Tree for Arithmetic Expression
    abstract_syn_tree = parser.arithmetic_expression_parser()
    syntax_error = abstract_syn_tree.error

    return tokens, abstract_syn_tree.node, syntax_error
