from .token import Token
from .constants import *
from .position import Position
from ..error_handler.illegal_char_err import IllegalCharError
from ..error_handler.expected_char_err import ExpectedCharError


class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.pos = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance_char()

    def advance_char(self):
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

            # LETTERS -> make_identifier
            if self.current_char in LETTERS:
                identifier = self.make_identifier_token()
                tokens.append(identifier)

            # DIGITS -> make_number_token
            elif self.current_char in DIGITS:
                number_token = self.make_number_token()
                tokens.append(number_token)

            # ignoring white spaces
            elif self.current_char in " \t":
                self.advance_char()

            # + TOKEN
            elif self.current_char == '+':
                plus_token = Token(TT_PLUS, '+', pos_start=self.pos)
                tokens.append(plus_token)
                self.advance_char()

            # - TOKEN
            elif self.current_char == '-':
                minus_token = Token(TT_MINUS, '-', pos_start=self.pos)
                tokens.append(minus_token)
                self.advance_char()

            # x TOKEN
            elif self.current_char == '*':
                mul_token = Token(TT_MUL, '*', pos_start=self.pos)
                tokens.append(mul_token)
                self.advance_char()

            # / TOKEN
            elif self.current_char == '/':
                div_token = Token(TT_DIV, '/', pos_start=self.pos)
                tokens.append(div_token)
                self.advance_char()

            # ^ TOKEN
            elif self.current_char == '^':
                div_token = Token(TT_POW, '^', pos_start=self.pos)
                tokens.append(div_token)
                self.advance_char()

            # ( TOKEN
            elif self.current_char == '(':
                left_paren_token = Token(TT_LPAREN, pos_start=self.pos)
                tokens.append(left_paren_token)
                self.advance_char()

            # COMPARISON OPERATORS TOKENS:
            # !=
            elif self.current_char == '!':
                not_eq_token, error_making_token = self.make_not_eq_token()
                if error_making_token:
                    return [], error_making_token
                tokens.append(not_eq_token)

            # == or =
            elif self.current_char == '=':
                eq_or_ee_token = self.make_eq_or_ee_token()
                tokens.append(eq_or_ee_token)

            # > or >=
            elif self.current_char == '>':
                gt_or_gte_token = self.make_gt_or_gte_token()
                tokens.append(gt_or_gte_token)

            # < or <=
            elif self.current_char == '<':
                lt_or_lte_token = self.make_lt_or_lte_token()
                tokens.append(lt_or_lte_token)

            # ) TOKEN
            elif self.current_char == ')':
                right_paren_token = Token(TT_RPAREN, pos_start=self.pos)
                tokens.append(right_paren_token)
                self.advance_char()

            # If curr_char read doesn't match any of the token_types of our lang
            # IllegalCharError:
            else:

                pos_start = self.pos.copy()  # get current Position object

                ill_char = self.current_char
                self.advance_char()
                # return empty token array and error
                return [], IllegalCharError(pos_start=pos_start, pos_end=self.pos, err_details="'" + ill_char + "'")

        # If no errors, return tokens array and None for error and add EOF token in the end of list of tokens
        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number_token(self):
        # to keep track of number:
        num_str = ''
        dot_count = 0  # for floating point numbers
        pos_start = self.pos.copy()
        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance_char()

        if dot_count == 0:
            int_token = Token(TT_INT, int(num_str), pos_start=pos_start, pos_end=self.pos)
            return int_token
        else:
            float_token = Token(TT_FLOAT, float(num_str), pos_start=pos_start, pos_end=self.pos)
            return float_token

    def make_identifier_token(self):
        id_str = ''

        # save the current pos as starting pos of id_token
        id_pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance_char()

        if id_str in KEYWORDS:
            id_tok_type = TT_KEYWORD
        else:
            id_tok_type = TT_IDENTIFIER

        id_token = Token(type_=id_tok_type, value=id_str, pos_start=id_pos_start, pos_end=self.pos)
        return id_token

    def make_not_eq_token(self):
        pos_start = self.pos.copy()
        self.advance_char()

        if self.current_char == '=':
            return Token(type_=TT_NE, value='!=', pos_start=pos_start, pos_end=self.pos), None
        else:
            self.advance_char()
            return None, ExpectedCharError(
                pos_start=pos_start,
                pos_end=self.pos,
                err_details="'=' (after '!')"
            )

    def make_eq_or_ee_token(self):
        pos_start = self.pos.copy()
        self.advance_char()

        if self.current_char == '=':
            self.advance_char()
            return Token(type_=TT_EE, value='==', pos_start=pos_start, pos_end=self.pos)

        else:
            return Token(type_=TT_EQ, value='=', pos_start=pos_start, pos_end=self.pos)

    def make_gt_or_gte_token(self):
        pos_start = self.pos.copy()
        self.advance_char()

        if self.current_char == '=':
            self.advance_char()
            return Token(type_=TT_GTE, value='>=', pos_start=pos_start, pos_end=self.pos)

        else:
            return Token(type_=TT_GT, value='>', pos_start=pos_start, pos_end=self.pos)

    def make_lt_or_lte_token(self):
        pos_start = self.pos.copy()
        self.advance_char()

        if self.current_char == '=':
            self.advance_char()
            return Token(type_=TT_LTE, value='<=', pos_start=pos_start, pos_end=self.pos)

        else:
            return Token(type_=TT_LT, value='<', pos_start=pos_start, pos_end=self.pos)
