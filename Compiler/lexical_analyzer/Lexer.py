##########################
# LEXER CLASS
##########################

from .Token import Token
from .constants import *
from .position import Position
from Compiler.error_handler.illegal_char_err import IllegalCharError as Ice


class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.pos = Position(-1, 0, 1, file_name, text)
        self.current_char = None
        self.advance()

    def advance(self):
        """
            advances pos to point to next character in the text
        """
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_token(self):
        """
            creates a Token object for every valid token of out lang and appends in the tokens[]

        Returns: array of Token objects

        """
        tokens = []

        # Scan each character to decide type of Token object to be created for it and create and append in tokens []:
        while self.current_char is not None:

            # DIGITS -> make_number_token
            if self.current_char in DIGITS:
                number_token = self.make_number_token
                tokens.append(number_token)

            # ignoring white spaces
            elif self.current_char in " \t":
                self.advance()

            # PLUS TOKEN
            elif self.current_char == '+':
                plus_token = Token(TT_PLUS)
                tokens.append(plus_token)
                self.advance()

            # MINUS TOKEN
            elif self.current_char == '-':
                minus_token = Token(TT_MINUS)
                tokens.append(minus_token)
                self.advance()

            # MUL TOKEN
            elif self.current_char == '*':
                mul_token = Token(TT_MUL)
                tokens.append(mul_token)
                self.advance()

            # DIV TOKEN
            elif self.current_char == '/':
                div_token = Token(TT_DIV)
                tokens.append(div_token)
                self.advance()

            # LPAREN TOKEN
            elif self.current_char == '(':
                left_paren_token = Token(TT_LPAREN)
                tokens.append(left_paren_token)
                self.advance()

            # RPAREN TOKEN
            elif self.current_char == ')':
                right_paren_token = Token(TT_RPAREN)
                tokens.append(right_paren_token)
                self.advance()

            # If curr_char read doesn't match any of the token_types of our lang
            # IllegalCharError:
            else:

                pos_start = self.pos.copy() # get current Position object

                ill_char = self.current_char
                self.advance()
                # return empty token array and error
                return [], Ice(pos_start=pos_start, pos_end=self.pos, err_details="'" + ill_char + "'")

        # If no errors, return tokens array and None for error
        return tokens, None

    @property
    def make_number_token(self):
        # to keep track of number:
        num_str = ''
        dot_count = 0  # for floating point numbers

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            int_token = Token(TT_INT, int(num_str))
            return int_token
        else:
            float_token = Token(TT_FLOAT, float(num_str))
            return float_token
