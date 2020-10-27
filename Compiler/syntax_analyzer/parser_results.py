class ParseResult:
    def __init__(self):
        self.node = None
        self.error = None

    def register(self, parse_result):
        if isinstance(parse_result, ParseResult):
            if parse_result.error:
                self.error = parse_result.error
            return parse_result.node

        return parse_result

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self
