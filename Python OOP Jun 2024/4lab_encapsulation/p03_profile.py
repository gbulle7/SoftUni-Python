class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, new_username):
        if len(new_username) < 5 or len(new_username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = new_username

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8 or new_password.lower() == new_password or not [x for x in new_password if x.isdigit()]:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = new_password

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
