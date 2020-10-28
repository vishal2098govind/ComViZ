from .error import Error
from .string_with_arrows import string_with_arrows


class InterpreterError(Error):
    """
      Raised while parsing in case of syntax error
    """

    def __init__(self, pos_start, pos_end, err_details, context):
        super().__init__(pos_start, pos_end, err_name="Runtime Error", err_details=err_details)
        self.context = context

    # over-ride as_string() method from Error
    def as_string(self):
        result = self.generate_traceback()
        result += f'{self.err_name}: {self.err_details}\n'
        result += '\n\n' + string_with_arrows(self.pos_start.file_text, self.pos_start, self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        context = self.context

        # for each part of the trace
        while context:
            result = f'   File {pos.file_name}, line {str(pos.line_no + 1)} in {context.curr_context_name}\n'+result
            pos = context.context_change_position
            context = context.parent_context_name

        return 'Traceback (most recent call last):\n' + result
