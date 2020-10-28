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
        self.pos_start = self.num_token.pos_start
        self.pos_end = num_token.pos_end

    def __repr__(self):
        """

        Returns: String representation of Node

        """
        return f'{self.num_token}'


class BinaryOperationNode:
    """
        Nodes for representing arithmetic operations +,-,*,/,^
    """
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_token}, {self.right_node})'


class UnaryOperationNode:
    def __init__(self, op_token, right_node):
        self.op_token = op_token
        self.right_node = right_node

        self.pos_start = self.op_token.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.op_token}, {self.right_node})'


class VariableAccessNode:
    def __init__(self, var_name_token):
        self.var_name_token = var_name_token

        self.pos_start = self.var_name_token.pos_start
        self.pos_end = self.var_name_token.pos_end

    def __repr__(self):
        return f'{self.var_name_token}'


class VariableAssignNode:
    def __init__(self, var_name_token, var_value_node):
        self.var_name_token = var_name_token
        self.var_value_node = var_value_node

        self.pos_start = self.var_name_token.pos_start
        self.pos_end = self.var_value_node.pos_end

    def __repr__(self):
        return f'{self.var_name_token} = {self.var_value_node}'
