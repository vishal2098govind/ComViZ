class Number:
    """
    To store numbers and operating on them with other numbers
    """

    def __init__(self, value):
        """
        Args:
            value: any number
        """
        self.value = value
        self.set_pos()

    def set_pos(self, pos_start=None,pos_end =None):
        """
        To indicate position while showing error messages
        Args:
            pos_start: starting of the number
            pos_end: ending of the number

        Returns: Number object
        """
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    # When number represented by self is to be added to any other Number object with a number
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(value=self.value + other.value)

    # When number represented by self is to be subtracted to any other Number object with a number
    def sub_by(self, other):
        if isinstance(other, Number):
            return Number(value=self.value - other.value)

    # When number represented by self is to be added to any other Number object with a number
    def multiplied_by(self, other):
        if isinstance(other, Number):
            return Number(value=self.value * other.value)

    # When number represented by self is to be added to any other Number object with a number
    def divided_by(self, other):
        if isinstance(other, Number):
            return Number(value=self.value / other.value)

    def __repr__(self):
        return str(self.value)