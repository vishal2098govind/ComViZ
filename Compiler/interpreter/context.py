class Context:
    """
        To hold the current context of the program
        and also send SymbolTable instance to the interpreter

        current context could be :
            function : if we are currently inside that function
            entire program : if we are not inside any function
    """

    def __init__(self, curr_context_name, parent_context_name=None, context_change_pos=None):
        self.curr_context_name = curr_context_name
        self.parent_context_name = parent_context_name
        self.context_change_position=context_change_pos
        self.symbol_table = None
