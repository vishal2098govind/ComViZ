from Compiler.interpreter.data_types import Number
from Compiler.lexical_analyzer.constants import *


class Interpreter:

    def visit_child_nodes(self, node, tokens=None):

        if tokens:
            print('Lexer Output: Tokens')
            print(tokens)
            print('Parser Output: Abstract Syntax Tree')
            print(node)

        # get method_name to visit child node depending on the type of node
        # If type of node passed is BinaryOperationNode,
        # method_name = visit_BinaryOperationNode
        method_name = f'visit_{type(node).__name__}'

        # get method to be invoked from method_name
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    # Define visit method for each of the node type:
    @staticmethod
    def visit_NumberNode(node):
        return Number(node.num_token.value).set_pos(node.pos_start, node.pos_end)

    def visit_BinaryOperationNode(self, node):

        left = self.visit_child_nodes(node.left_num_node)
        right = self.visit_child_nodes(node.right_num_node)

        result = None

        if node.op_token.type == TT_PLUS:
            result = left.added_to(right)
        elif node.op_token.type == TT_MINUS:
            result = left.subtracted_by(right)
        elif node.op_token.type == TT_MUL:
            result = left.multiplied_by(right)
        elif node.op_token.type == TT_DIV:
            result = left.divided_by(right)

        return result.set_pos(node.pos_start, node.pos_end)

    def visit_UnaryOperationNode(self, node):
        number = self.visit_child_nodes(node.node)

        if node.op_token.type == TT_MINUS:
            number = number.multiplied_by(Number(-1))

        return number.set_pos(node.pos_start, node.pos_end)
