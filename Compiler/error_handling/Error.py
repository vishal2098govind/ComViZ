class Error:

    def __init__(self, err_name, err_details):
        self.err_name = err_name
        self.err_details = err_details

    def as_string(self):
        result = f'{self.err_name}: {self.err_details}'
        return result
