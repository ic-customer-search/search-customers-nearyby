class InvalidFormatException(Exception):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        if self.message != "":
            return self.message
        return "Format of the string is invalid"


class InvalidResponseException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "%s: %s" % (self.code, self.message)
