##########################
# LEXER CLASS
##########################

from Token import *
from constants import *


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(
            self.text) else None

    def make_token(self):
        tokens = []

        while self.current_char != None:

            # DIGITS
            if self.current_char in DIGITS:
                number_token = self.make_number_token()
                tokens.append(number_token)

            # ignoring white spaces
            if self.current_char in ' \t':
                self.advance()

            # PLUS TOKEN
            elif self.current_char == '+':
                plus_token = Token(TT_PLUS)
                tokens.append(plus_token)

            # MINUS TOKEN
            elif self.current_char == '-':
                minus_token = Token(TT_MINUS)
                tokens.append(minus_token)

            # MUL TOKEN
            elif self.current_char == '*':
                mul_token = Token(TT_MUL)
                tokens.append(mul_token)

            # DIV TOKEN
            elif self.current_char == '/':
                div_token = Token(TT_DIV)
                tokens.append(div_token)

            # LPAREN TOKEN
            elif self.current_char == '(':
                left_paran_token = Token(TT_LPAREN)
                tokens.append(left_paran_token)

            # RPAREN TOKEN
            elif self.current_char == ')':
                right_paren_token = Token(TT_RPAREN)
                tokens.append(right_paren_token)

            # If curr_char read doesn't match any of the token_types of our lang
            # ERROR HANDLING

        return tokens

    def make_number_token(self):
        # to keep track of number:
        num_str = ''
        dot_count = 0  # for floating point numbers

        # while current char is (DIGIT or dot) and not None, concat to num_str
        while self.current_char != None and self.current_char in DIGITS + '.':

            # If the curr_char read is '.'
            if self.current_char == '.':

                # if we see more than 1 dot => break as a num can't have >1 dots
                if dot_count == 1:
                    break

                dot_count += 1
                # Add '.' to the num_str
                num_str += '.'

            # If curr_char read is NOT '.'
            else:

                # concat curr_char read, which will be a digit, to the num_str
                num_str += self.current_char

        # after getting num_str

        # if dot_count = 0 => num_str is an integer constant
        # thus create an INT token for the num_str, and return
        if dot_count == 0:
            int_token = Token(TT_INT, int(num_str))
            return int_token

        # if dot_count = 1 => num_str is an floating point constant
        # thus create an FLOAT token for the num_str, and return
        else:
            float_token = Token(TT_FLOAT, float(num_str))
            return float_token
