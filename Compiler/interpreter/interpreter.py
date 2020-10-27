from Compiler.interpreter.runtime_result import RuntimeResult
from Compiler.interpreter.data_types import Number
from Compiler.lexical_analyzer.constants import *


class Interpreter:

    def evaluate_node(self, node):
        """
            To Do a Post-Order Traversal abstract_syntax_tree obtained from parser
            Args:
                node: right_node to explore
            Returns:
                on success: RuntimeResult(error=None, result=Number(num_node.num_token.value))
                on failure: RuntimeResult(error=InterpreterError(), result=Number instance)
        """

        # get node_name_to_be_evaluated to visit child node and evaluate, depending on the type of node
        # If type of node passed is BinaryOperationNode,
        # node_name_to_be_evaluated = evaluate_BinaryOperationNode
        node_name_to_be_evaluated = f'evaluate_{type(node).__name__}'

        # get node_to_be_evaluated to be invoked from node_name_to_be_evaluated
        node_to_be_evaluated = getattr(self, node_name_to_be_evaluated, self.no_eval_method)

        return node_to_be_evaluated(node)

    # Define visit method for each of the node type possible in an abstract_syntax_tree obtained from parser:

    @staticmethod
    # NumberNode
    # To create terminal of number like INT or FLOAT
    def evaluate_NumberNode(num_node):
        """
        Args:
            num_node: instance of NumberNode

        Returns:
            on success: instance of RuntimeResult(result=
        """

        runtime_result = RuntimeResult()

        number = Number(value=num_node.num_token.value)

        number.set_pos(
            pos_start=num_node.pos_start,
            pos_end=num_node.pos_end
        )

        return runtime_result.success(result=number)

    # BinaryOperationNode
    # To evaluate T+T, T-T, F*F, F/F, A^F
    def evaluate_BinaryOperationNode(self, bin_op_node):  # Post-Order traversal of abstract_syntax_tree
        """
        Args:
            bin_op_node: op_token

        Returns:
            on success: RuntimeResult(result=Number(num_node.num_token.value), error=None)
            on failure: RuntimeResult(result=Number instance, error=InterpreterError())
        """

        runtime_result = RuntimeResult()

        left_node = runtime_result.register(runtime_result=self.evaluate_node(node=bin_op_node.left_node))

        right_node = runtime_result.register(runtime_result=self.evaluate_node(node=bin_op_node.right_node))

        if runtime_result.error:
            return runtime_result

        bin_op_result_node, runtime_error = None, None

        if bin_op_node.op_token.type == TT_PLUS:
            bin_op_result_node, runtime_error = left_node.added_to(right_node)
        elif bin_op_node.op_token.type == TT_MINUS:
            bin_op_result_node, runtime_error = left_node.subtracted_by(right_node)
        elif bin_op_node.op_token.type == TT_MUL:
            bin_op_result_node, runtime_error = left_node.multiplied_by(right_node)
        elif bin_op_node.op_token.type == TT_DIV:
            bin_op_result_node, runtime_error = left_node.divided_by(right_node)
        elif bin_op_node.op_token.type == TT_POW:
            bin_op_result_node, runtime_error = left_node.raised_to(right_node)

        if runtime_error:
            return runtime_result.failure(error=runtime_error)

        else:
            bin_op_result_node.set_pos(
                pos_start=bin_op_node.pos_start,
                pos_end=bin_op_node.pos_end
            )
            return runtime_result.success(result=bin_op_result_node)

    # UnaryOperationNode
    # To evaluate unary-minus operation like -5
    def evaluate_UnaryOperationNode(self, unary_node):

        runtime_result = RuntimeResult()

        number = runtime_result.register(runtime_result=self.evaluate_node(unary_node.right_node))

        if runtime_result.error:
            return runtime_result

        runtime_error = None

        if unary_node.op_token.type == TT_MINUS:  # -
            number, runtime_error = number.multiplied_by(Number(-1))  # -4 = -1*4

        if runtime_error:
            return runtime_result.failure(error=runtime_error)

        else:
            number.set_pos(
                pos_start=unary_node.pos_start,
                pos_end=unary_node.pos_end
            )
            return runtime_result.success(result=number)

    def no_eval_method(self, node):
        raise Exception(f'No eval_{type(node).__name__} method defined')
