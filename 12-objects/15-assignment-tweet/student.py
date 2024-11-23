class Tweet:
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length

        if max_length < 1:
            raise ValueError("the max_length should at least be 1")

    @property
    def message(self):
        return self.__message[:self.__max_length]

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, value):
        if value < 1:
            raise ValueError("the max_length should at least be 1")

        self.__max_length = value