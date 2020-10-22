from Compiler.error_handler.invalid_syntax_err import InvalidSyntaxError
from Compiler.lexical_analyzer.constants import *
from Compiler.syntax_analyzer.nodes import NumberNode, BinaryOperationNode
from Compiler.syntax_analyzer.parser_results import ParseResult


class Parser:

    def __init__(self, token_list):
        """
        Args:
            token_list: token list from Lexer
        """
        self.token_list = token_list
        self.curr_token_index = -1
        self.curr_token = None
        self.advance_token()

    def advance_token(self):
        self.curr_token_index += 1

        if self.curr_token_index < len(self.token_list):
            self.curr_token = self.token_list[self.curr_token_index]

        return self.curr_token

    # Parser for Arithmetic Expression Grammar
    # E -> l_T ((PLUS or MINUS) r_T)* , T -> l_F ( (MUL or DIV) r_F)* , F -> INT | FLOAT

    # For each of the non-terminal , we define a method
    def arithmetic_expression(self):
        """
        expression -> left_term_node ( ( PLUS or MINUS ) right_term_node )*
        Returns: BinaryOperationNode(left_term_node, MUL or DIV , right_term_node)
        """
        return self.binary_operation_node(rule=self.term, op_token_tuple=(TT_PLUS, TT_MINUS))

    def term(self):
        """
        term -> left_factor_node ( ( MUL or DIV ) right_factor_node )*
        Returns: BinaryOperationNode(left_factor_node, MUL or DIV , right_factor_node)
        """
        return self.binary_operation_node(rule=self.factor, op_token_tuple=(TT_MUL, TT_DIV))

    def factor(self):
        """
        factor -> INT Token | FLOAT Token

        Returns: If Token Type TT of the Token object with self.curr_token is TT_INT or TT_FLOAT , return a NumberNode
        object of that token

        """
        result = ParseResult()
        curr_tok = self.curr_token
        if self.curr_token.type in (TT_INT, TT_FLOAT):
            result.register(self.advance_token())
            return result.success(NumberNode(num_token=curr_tok))

        else:
            # if self.curr_token.type is not TT_INT or TT_FLOAT => Syntax Error
            return result.failure(InvalidSyntaxError(
                curr_tok.pos_start, curr_tok.pos_end,
                "Expected int or float type"
            ))

    def binary_operation_node(self, rule, op_token_tuple):
        """
        Args:
            rule: self.factor or self.term
            op_token_tuple: (TT_MUL, TT_DIV) or (TT_PLUS, TT_MINUS)

        Returns: BinaryOperationNode(left_node, op, right_node)
        """
        # left_node
        result = ParseResult()
        left_node = result.register(rule())  # self.factor or self.term which will return a NumberNode or
        # BinaryOperationNode
        if result.error:
            return result

        # ((MUL/PLUS or DIV/MINUS) right_node)*
        while self.curr_token.type in op_token_tuple:
            op_token = self.curr_token
            result.register(self.advance_token())

            right_node = result.register(rule())  # self.factor or self.term which will return a NumberNode or
            # BinaryOperationNode
            if result.error:
                return result
            # Create a BinaryOperation Node for op_token
            left_node = BinaryOperationNode(left_num_node=left_node, op_token=op_token,
                                            right_num_node=right_node)

        return result.success(left_node)  # finally left_node would be pointing to root of the binary_opn_tree

    # Parse the arithmetic expression
    def arithmetic_expression_parser(self):
        """
        Returns: Abstract syntax Tree
        """
        abstract_syntax_tree = self.arithmetic_expression()

        if not abstract_syntax_tree.error and self.curr_token.type != TT_EOF:
            return abstract_syntax_tree.failure(InvalidSyntaxError(
                self.curr_token.pos_start,
                self.curr_token.pos_end,
                "Expected '+', '-', '*' or '/'"
            ))

        return abstract_syntax_tree
