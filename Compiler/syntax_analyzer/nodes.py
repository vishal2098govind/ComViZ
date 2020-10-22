class NumberNode:
    """
    Nodes for representing Number Tokens i.e. TT_INT or TT_FLOAT
    """
    def __init__(self, num_token):
        """

        Args:
            num_token: Token object of TT_INT or TT_FLOAT
        """
        self.num_token = num_token

    def __repr__(self):
        """

        Returns: String representation of Node

        """
        return f'{self.num_token}'


class BinaryOperationNode:
    """
    Nodes for representing arithmetic operations +,-,*,/
    """
    def __init__(self, left_num_node, op_token, right_num_node):
        self.left_num_node = left_num_node
        self.op_token = op_token
        self.right_num_node = right_num_node

    def __repr__(self):
        return f'({self.left_num_node}, {self.op_token}, {self.right_num_node})'
