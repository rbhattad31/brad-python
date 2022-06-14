class Suc:
    string = ''

    def get_string(self):
        self.string = input('enter a string')

    def print_string(self):
        print(self.string.upper())


obj = Suc()
obj.get_string()
obj.print_string()
