class PySolution:
    @staticmethod
    def int_to_roman(num):

        integer = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]

        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

        roman_num = ''

        i = 0

        while num > 0:
            for _ in range(num // integer[i]):
                print("_ is", _)
                print("num is", num)
                print("integer is", integer[i])
                print("floor division value is", num // integer[i])
                roman_num += roman[i]
                num -= integer[i]
            i += 1
        return roman_num


number = int(input("Enter the number: "))

print(PySolution().int_to_roman(number))
