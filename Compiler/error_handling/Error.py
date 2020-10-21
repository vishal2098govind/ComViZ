class Error:

    def __init__(self, pos_start, pos_end, err_name, err_details):
        self.pos_start=pos_start
        self.pos_end=pos_end
        self.err_name = err_name
        self.err_details = err_details

    def as_string(self):
        result = f'{self.err_name}: {self.err_details}\n'
        result += f'File {self.pos_start.file_name}, line {self.pos_start.line_no + 1}'
        return result
