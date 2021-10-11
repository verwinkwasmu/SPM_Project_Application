
class User:
    def __init__(self, userId, userName="", email="", password="", userType=""):
        self.userId = userId
        self.userName = userName
        self.email = email
        self.password = userType

    def get_userId(self):
        return self.userId
    
    def get_userName(self):
        return self.name

    def get_email(self):
        return self.email

    def get_userType(self):
        return self.userType
