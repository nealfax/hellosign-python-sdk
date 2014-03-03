from http.request import HSRequest
from resource.account import Account

class HSClient(object):
	"""docstring for HSClient"""
	ACCOUNT_CREATE_URL = 'https://api.hellosign.com/v3/account/create'
	ACCOUNT_INFO_URL = 'https://api.hellosign.com/v3/account'
	ACCOUNT_UPDATE_URL = 'https://api.hellosign.com/v3/account'

	SIGNATURE_REQUEST_INFO_URL = 'https://api.hellosign.com/v3/signature_request/'
	SIGNATURE_REQUEST_LIST_URL = 'https://api.hellosign.com/v3/signature_request/list'

	# TODO: Put api account in HSClient's __init__ function instead of HSRequest

	def __init__(self):
		super(HSClient, self).__init__()
		self.account = Account()
		self.get_account_info()


	def create_account(self, email, password):
		# TODO: make the check exceptions
		if email is None:
			print ("Email is not valid")
		if password is None:
			print ("Password is not valid")
		request = HSRequest()
		response = request.post(self.ACCOUNT_CREATE_URL, {'email_address': email, 'password': password})
		# print response
		return Account(response["account"])
		
	# Get account info and put in self.account
	def get_account_info(self):
		request = HSRequest()
		response = request.get(self.ACCOUNT_INFO_URL)
		# self.account = Account(response, "account")
		self.account.json_data = response["account"]

	def update_account_info(self):
		request = HSRequest()
		request.post(self.ACCOUNT_UPDATE_URL, {'callback_url': self.account.callback_url})
		# return response

	# Get a signature request
	# param @signature_request_id
	def get_signature_request(self, signature_request_id):
		request = HSRequest()
		response = request.get(self.SIGNATURE_REQUEST_INFO_URL + signature_request_id)
		return SignatureRequest(response["signature_request"])

	def get_signature_request_list(self):
		list = []
		request = HSRequest()
		response = request.get(self.SIGNATURE_REQUEST_LIST_URL)
		print response