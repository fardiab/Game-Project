import json

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        self.serialize()

    def __str__(self):
        return f"{self.username} {self.email} {self.__password}"

    def serialize(self):
        return {
            'name': self.username,
            'email': self.email,
            'password': self.__password
        }

    def to_json(self):
        try:
            with open("registerdb.json", 'r+') as f:
                arr = json.load(f)
                for i in arr:
                    if i['name'] == self.username:
                        return "User already exists"
                f.seek(0)
                arr.append(self.serialize())
                json.dump(arr, f)
        except:
            with open("registerdb.json", 'w') as f:
                json.dump([self.serialize()], f)
        return "User added"


