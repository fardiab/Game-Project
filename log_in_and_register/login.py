class LogIn():
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def __str__(self):
        return "You log in successfullly"