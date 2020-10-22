class ParseResult:
    """
    To check for errors while parsing
    """

    def __init__(self):
        self.error = None
        self.node = None

    def register(self, result):
        if isinstance(result, ParseResult):
            if result.error:
                self.error = result.error
            return result.node

        # else it should be node
        return result

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self
