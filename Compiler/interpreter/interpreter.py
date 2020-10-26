from Compiler.interpreter.RuntimeResult import RuntimeResult
from Compiler.interpreter.data_types import Number
from Compiler.lexical_analyzer.constants import *


class Interpreter:

    def visit_child_nodes(self, node):

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
        return RuntimeResult().success(
            Number(node.num_token.value).set_pos(node.pos_start, node.pos_end)
        )

    def visit_BinaryOperationNode(self, node):

        runtime_result = RuntimeResult()

        left = runtime_result.register(self.visit_child_nodes(node.left_num_node))
        right = runtime_result.register(self.visit_child_nodes(node.right_num_node))

        if runtime_result.error: return runtime_result
        result = None

        if node.op_token.type == TT_PLUS:
            result, runtime_error = left.added_to(right)
        elif node.op_token.type == TT_MINUS:
            result, runtime_error = left.subtracted_by(right)
        elif node.op_token.type == TT_MUL:
            result, runtime_error = left.multiplied_by(right)
        elif node.op_token.type == TT_DIV:
            result, runtime_error = left.divided_by(right)

        if runtime_error:
            return runtime_result.failure(runtime_error)
        else:
            return runtime_result.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOperationNode(self, node):
        runtime_result = RuntimeResult()

        number = runtime_result.register(self.visit_child_nodes(node.node))

        if runtime_result.error:
            return runtime_result

        runtime_error = None

        if node.op_token.type == TT_MINUS:
            number, runtime_error = number.multiplied_by(Number(-1))

        if runtime_error:
            return runtime_result.failure(runtime_error)
        else:
            return runtime_result.success(number.set_pos(node.pos_start, node.pos_end))
