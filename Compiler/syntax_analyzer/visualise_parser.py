from anytree import AnyNode
from Compiler.error_handler.invalid_syntax_err import InvalidSyntaxError
from Compiler.lexical_analyzer.constants import *
from Compiler.syntax_analyzer.nodes import NumberNode, BinaryOperationNode, UnaryOperationNode
from Compiler.syntax_analyzer.parser_results import ParseResult
from Visualiser.visualise_pt import visualize_parse_tree


class VisualiseParser:
    """
        # VisualiseParser for Arithmetic Expression Grammar
        # E -> l_T ((PLUS_Token or MINUS_Token) r_T)* ,
        # T -> l_F ((MUL_Token or DIV_Token) r_F)* ,
        # F -> PLUS_Token F | MINUS_Token F | P,
        # P -> A (POW_Token F)*
        # A -> INT_Token | FLOAT_Token | (_Token E )_Token
    """

    def visualize_parse_tree(self):
        # if False:
        visualize_parse_tree(trace=self.trace)

    def __init__(self, token_list):
        """
        Args:
            token_list: list of tokens from Lexer
        """
        self.token_list = token_list
        self.curr_token_index = -1
        self.curr_token = None
        self.advance_token()
        self.trace = []

    def advance_token(self, caller=None):
        prev_tok = self.curr_token

        if caller and prev_tok.type in (TT_INT, TT_FLOAT, TT_DIV, TT_POW, TT_MUL, TT_LPAREN, TT_MINUS, TT_RPAREN,
                                        TT_PLUS):
            terminal_node = AnyNode(name=prev_tok, parent=caller)
            self.trace.append(terminal_node)
            self.visualize_parse_tree()

        self.curr_token_index += 1

        if self.curr_token_index < len(self.token_list):
            self.curr_token = self.token_list[self.curr_token_index]

        return self.curr_token

    # Parse the arithmetic expression
    def arith_exp_parser(self):
        """
        Returns:
            on success: ParseResult(node=root of abstract_syntax_tree obtained, error=None)
            on failure: ParseResult(node=Node instance, error=InvalidSyntaxError())
        """
        parse_result = self.arith_exp()

        if not parse_result.error and self.curr_token.type != TT_EOF:
            return parse_result.failure(InvalidSyntaxError(
                self.curr_token.pos_start,
                self.curr_token.pos_end,
                "Expected '+', '-', '*' or '/'"
            ))

        return parse_result

    # Every _Token is a terminal
    # For each of the non-terminal , we define a method:

    # E -> l_T ((PLUS_Token or MINUS_Token) r_T)*  // Binary Operation
    def arith_exp(self, caller=None):  # E
        """
        expression -> left_term_node ( ( PLUS or MINUS ) right_term_node )*

        Returns:
            on success: ParseResult(node=BinaryOperationNode(left_rule_node, op_token, right_rule_node), error=None)
            on failure: ParseResult(node=Node instance, error=InvalidSyntaxError())
        """
        non_terminal_node = AnyNode(id='E' + str(len(self.trace)), name='E', parent=caller)
        self.trace.append(non_terminal_node)
        self.visualize_parse_tree()
        return self.binary_operation_node(
            left_rule=self.term,
            op_token_tuple=(TT_PLUS, TT_MINUS),
            right_rule=self.term,
            caller=non_terminal_node
        )

    # T -> l_F ((MUL_Token or DIV_Token) r_F)*     // Binary Operation
    def term(self, caller):  # T
        """
        term -> left_factor_node ( ( MUL_Token or DIV_Token ) right_factor_node )*

        Returns:
            on success: ParseResult(node=BinaryOperationNode(left_rule_node, op_token, right_rule_node), error=None)
            on failure: ParseResult(node=Node instance, error=InvalidSyntaxError())
        """
        non_terminal_node = AnyNode(id='T' + str(len(self.trace)), name='T', parent=caller)
        self.trace.append(non_terminal_node)
        self.visualize_parse_tree()
        return self.binary_operation_node(
            left_rule=self.factor,
            op_token_tuple=(TT_MUL, TT_DIV),
            right_rule=self.factor,
            caller=non_terminal_node
        )

    # F -> PLUS_Token F | MINUS_Token F | P        // Unary Operation
    def factor(self, caller):  # F
        """
        factor -> PLUS_Token power | MINUS_Token power | power

        Returns:
                for factor-> PLUS_Token power| MINUS_Token power:
                    on success: ParseResult(node=UnaryOperationNode(curr_tok, right_factor_node), error=None)
                    on failure: ParseResult(node=BinaryOperationNode(), error=InvalidSyntaxError())
        """
        non_terminal_node = AnyNode(id='F' + str(len(self.trace)), name='F', parent=caller)
        self.trace.append(non_terminal_node)
        self.visualize_parse_tree()
        parse_result = ParseResult()
        curr_tok = self.curr_token

        # F -> PLUS_Token F | MINUS_Token F        // Unary Operation
        if self.curr_token.type in (TT_PLUS, TT_MINUS):
            parse_result.register(self.advance_token(caller=non_terminal_node))  # register PLUS or MINUS

            right_factor_node = parse_result.register(self.factor(caller=non_terminal_node))

            if parse_result.error:
                return parse_result
            else:
                return parse_result.success(
                    node=UnaryOperationNode(
                        op_token=curr_tok,
                        right_node=right_factor_node
                    )
                )

        # F -> P                                    // Unit Production
        else:
            return self.power(caller=non_terminal_node)

    # P -> A (POW_Token F)*                        // Binary Operation
    def power(self, caller):  # P
        """
        P -> A ( POW_Token F )*

        Returns:
            on success: ParseResult(node=BinaryOperationNode(left_rule_node, op_token, right_rule_node), error=None)
            on failure: ParseResult(node=Node, error=InvalidSyntaxError())
        """
        non_terminal_node = AnyNode(id='P' + str(len(self.trace)), name='P', parent=caller)
        self.trace.append(non_terminal_node)
        self.visualize_parse_tree()
        return self.binary_operation_node(
            left_rule=self.atom,
            op_token_tuple=(TT_POW,),
            right_rule=self.factor,
            caller=non_terminal_node
        )

    # A -> INT_Token | FLOAT_Token | (_Token E )_Token
    def atom(self, caller):  # A
        """
        A -> INT_Token | FLOAT_Token | (_Token E )_Token
        Returns:
                for atom-> INT-Token | FLOAT_Token:
                    on success: ParseResult( node=NumberNode(curr_token), error=None) object

                for atom-> (_Token arith_exp )_Token:
                    on success: ParseResult( node=arith_exp_node, error=None) object
                    on failure: ParseResult( node=Node instance, error=InvalidSyntax("expected )") object

                on failure: ParseResult(node = Node instance, error=InvalidSyntax("expected INT or FLOAT or (")) object
        """
        non_terminal_node = AnyNode(id='A' + str(len(self.trace)), name='A', parent=caller)
        self.trace.append(non_terminal_node)
        self.visualize_parse_tree()
        parse_result = ParseResult()
        curr_tok = self.curr_token

        # A -> INT_Token | FLOAT_Token
        # A returns ParseResult(node=NumberToken(INT_Token), error=None) object to its caller
        if curr_tok.type in (TT_INT, TT_FLOAT):
            parse_result.register(self.advance_token(caller=non_terminal_node))  # INT_Token or FLOAT_Token

            # return ParseResult(node=NumberNode(curr_token), error=None) object to caller of self.atom()
            return parse_result.success(node=NumberNode(num_token=curr_tok))

        # A -> (_Token E )_Token
        # A returns ParseResult(node = arith_exp_node, error=None) object to its caller
        elif curr_tok.type == TT_LPAREN:
            parse_result.register(self.advance_token(caller=non_terminal_node))  # (
            arith_exp_node = parse_result.register(self.arith_exp(caller=non_terminal_node))  # E

            if parse_result.error:
                return parse_result

            if self.curr_token.type == TT_RPAREN:
                parse_result.register(self.advance_token(caller=non_terminal_node))  # )

                # return ParseResult(node = arith_exp_node, error = None)
                return parse_result.success(node=arith_exp_node)

            # else Syntax Error
            else:
                return parse_result.failure(
                    error=InvalidSyntaxError(
                        pos_start=curr_tok.pos_start,
                        pos_end=curr_tok.pos_end,
                        err_details="Expected )"
                    ))

        # else Syntax Error
        else:
            return parse_result.failure(
                error=InvalidSyntaxError(
                    pos_start=curr_tok.pos_start,
                    pos_end=curr_tok.pos_end,
                    err_details="Expected INT or FLOAT or '+' or '-' or ("
                )
            )

    # left_terminal -> left_rule ((MUL/PLUS or DIV/MINUS or POW) right_rule)*
    def binary_operation_node(self, left_rule, op_token_tuple, right_rule, caller):
        """
            left_terminal -> left_rule ( (op_token,) right_rule )*

            For Binary Operation Terminals i.e. E, T, P:
            Utility for self.arith_exp , self.term, self.power because all these are binary operation nodes

        Args:
            caller: Parent
            left_rule: self.factor or self.term or self.atom
            op_token_tuple: (TT_MUL, TT_DIV) or (TT_PLUS, TT_MINUS) or (TT_POW,)
            right_rule: self.factor or self.term

        Returns:
            on success: ParseResult(node=BinaryOperationNode(left_rule_node, op_token, right_rule_node), error=None)
            on failure: ParseResult(node=BinaryOperationNode(), error=InvalidSyntaxError())
        """
        parse_result = ParseResult()
        left_rule_node = parse_result.register(left_rule(caller=caller))  # left_rule

        if parse_result.error:
            return parse_result

        while self.curr_token.type in op_token_tuple:  # ((MUL/PLUS or DIV/MINUS or POW) right_rule)*
            op_token = self.curr_token
            parse_result.register(self.advance_token(caller=caller))  # (MUL/PLUS or DIV/MINUS or POW)

            right_rule_node = parse_result.register(right_rule(caller=caller))  # right_rule

            if parse_result.error:
                return parse_result

            left_rule_node = BinaryOperationNode(
                left_node=left_rule_node,
                op_token=op_token,
                right_node=right_rule_node
            )

        return parse_result.success(node=left_rule_node)
