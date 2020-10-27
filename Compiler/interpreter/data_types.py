from Compiler.error_handler.runtime_err import InterpreterError


class Number:
    """
        To store numbers and operating on them with other numbers
    """

    def __init__(self, value):
        """
        Args:
            value: any number ( Token().value i.e. value part of a Token() object of type = INT or FLOAT )
        """
        self.value = value
        self.pos_start = None
        self.pos_end = None
        self.set_pos()

    def set_pos(self, pos_start=None, pos_end=None):
        """
            To indicate position while showing error messages
        Args:
            pos_start: starting of the number
            pos_end: ending of the number

        Returns: self
        """
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    # Operations on Number data type:

    # When number represented by self is to be added to any other Number object with a number
    def added_to(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value + other_operand.value), None

    # When number represented by self is to be subtracted to any other Number object with a number
    def subtracted_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value - other_operand.value), None

    # When number represented by self is to be added to any other Number object with a number
    def multiplied_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value * other_operand.value), None

    # When number represented by self is to be added to any other Number object with a number
    def divided_by(self, other_operand):
        if isinstance(other_operand, Number):
            if other_operand.value == 0:
                return None, InterpreterError(
                    other_operand.pos_start, other_operand.pos_end,
                    'Division by zero'
                )
            return Number(value=self.value / other_operand.value), None

    # When number represented by self is to be raised to any other Number object with a number
    def raised_to(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value**other_operand.value), None

    def __repr__(self):
        return str(self.value)
