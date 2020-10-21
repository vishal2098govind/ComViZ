##########################
# TOKENS CLASS
##########################
print('token class')


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value != None:
            return f'{self.type}: {self.value}'
        else:
            return f'{self.type}'
