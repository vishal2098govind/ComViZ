class SymbolTable:
    """
        To keep track of all the variable names or identifiers and their values
        Along with keeping track of parent symbol table

        For every function invocation, a new SymbolTable instance is created for that function
        SymbolTable corresponding to a function will have variables and values which have been assigned within that
        corresponding function
        Once that corresponding function is completed, then the SymbolTable instance corresponding to that function
        will be removed

        Every function will have a parent SymbolTable which will be the global-SymbolTable instance which will have
        all the global variables in the program as they can be accessed from anywhere within the program

        Thus, we need parent_symbol_table for functions
    """

    def __init__(self):
        self.symbols_map = {"var": [], "var_value": [], "context": []}
        self.parent_symbol_table = None

    def get_var_value(self, var_name):
        value = self.symbols_map["var_value"][self.symbols_map["var"].index(var_name)]
        # if value is not found in own symbol_table, we have to search in parent_symbol_table

        if value is None and self.parent_symbol_table is not None:
            return self.parent_symbol_table.get(var_name)

        else:
            return value

    def set_var_value(self, var_name, new_var_value, context_name):
        self.symbols_map["var"].append(var_name)
        self.symbols_map["var_value"].append(new_var_value)
        self.symbols_map["context"].append(context_name)

    def remove_var_entry(self, var_name):
        del self.symbols_map[var_name]

    def __repr__(self):
        return f'{self.symbols_map}\n{self.parent_symbol_table}'
