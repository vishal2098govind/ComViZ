class ParseResult:
    def __init__(self):
        self.node = None
        self.error = None
        self.advance_count = 0

    def register_advancement(self):
        self.advance_count += 1

    def register(self, parse_result):
        self.advance_count += parse_result.advance_count
        if parse_result.error:
            self.error = parse_result.error
        return parse_result.node

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error and self.advance_count == 0:
            self.error = error
        return self
