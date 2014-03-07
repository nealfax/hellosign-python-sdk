class Authentication(object):

    email = ""
    password = ""
    apiKey = ""
    accessToken = ""
    accessTokenType = ""

    def set_credentials(self, email, password):
        if email is None:
            print ("Email cannot be null")
        if password is None:
            print("Password cannot be null")
        self.email = email
        self.password = password
