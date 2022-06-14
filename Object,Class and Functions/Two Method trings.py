class IOString:
    def __init__(self):
        self.first_string = ""

    def get_String(self):
        self.first_string = input()

    def print_String(self):
        print(self.first_string.upper())

first_string = IOString()
first_string.get_String()
first_string.print_String()