from .error import Error


class InterpreterError(Error):
    """
      Raised while parsing in case of syntax error
    """

    def __init__(self, pos_start, pos_end, err_details):
        super().__init__(pos_start, pos_end, err_name="Runtime Error", err_details=err_details)
