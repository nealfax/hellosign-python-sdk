import os
import requests

class Authentication(object):

	email = ""
	password = ""
	apiKey = ""
	accessToken = ""
	accessTokenType = ""

	def set_credentials(self, email, password):
		if email == None:
			print ("Email cannot be null")
			end
		if password == None:
			print("Password cannot be null");
		}
		self.email = email
		self.password = password

	# def authenticate(self, url):

