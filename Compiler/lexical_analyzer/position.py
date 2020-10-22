##########################
# POSITION CLASS
##########################

class Position():
    """
        To keep track of line no, col no, index, file_name and file_text of each char
        Useful to point exact location of errors
    """

    def __init__(self, index, line_no, col_no, file_name, file_text):
        self.index = index
        self.line_no = line_no
        self.col_no = col_no
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_char):
        self.index += 1
        self.col_no += 1

        if current_char == '\n':
            self.line_no += 1
            self.col_no = 0

    def copy(self):
        return Position(self.index, self.line_no, self.col_no, self.file_name, self.file_text)
