class RuntimeResult:
    def __init__(self):
        """
            self.result: instance of data_types  ( like Number(), )
            self.error: instance of InterpreterError
        """
        self.result = None
        self.error = None

    def register(self, runtime_result):

        if runtime_result.error:
            self.error = runtime_result.error

        return runtime_result.result

    def success(self, result):

        self.result = result
        return self

    def failure(self, error):

        self.error = error
        return self
