from Compiler.error_handler.error import Error


class ExpectedCharError(Error):
    def __init__(self, pos_start, pos_end, err_details):
        super().__init__(pos_start, pos_end, err_name="Expected Character", err_details=err_details)
