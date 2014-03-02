from http.request import HSRequest
from resource.account import Account

class HSClient(object):
	"""docstring for HSClient"""
	ACCOUNT_CREATE_URL = 'https://api.hellosign.com/v3/account/create'

	# def __init__(self, arg):
	# 	super(HSClient, self).__init__()
	# 	self.arg = arg
	# 	self.account = Account()


	def create_account(self, email, password):
		# TODO: 
		if email is None:
			print ("Email is not valid")
		if password is None:
			print ("Password is not valid")
		request = HSRequest()
		response = request.post(self.ACCOUNT_CREATE_URL, {'email_address': email, 'password': password})
		return Account(response)
		