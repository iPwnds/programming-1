
class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        if string == self.__password:
            return True
        else:
            return False