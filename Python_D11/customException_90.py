class NotEligibleException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class EligibleException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Voteaccess:
    def __init__(self, age):
        self.__age = age

    def caste_vote(self):
        if self.__age > 18:

            raise EligibleException("you can vote!")
        elif self.__age < 18:

            raise NotEligibleException("you are not eligible for vote")


ui = int(input("Enter your age"))
access = Voteaccess(ui)
access.caste_vote()
