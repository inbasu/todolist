class PassByReference:
    def __init__(self):
        self.variable = True
        self.change(self.variable)
        print(self.variable)

    def change(self, var):
        var = not var


PassByReference()
