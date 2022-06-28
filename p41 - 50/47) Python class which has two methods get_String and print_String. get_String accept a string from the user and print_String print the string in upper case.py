class GetAndPrintString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter the string:")

    def print_string(self):
        print(self.string.upper())


GetAndPrintString()
GetAndPrintString().get_string()
GetAndPrintString().print_string()
