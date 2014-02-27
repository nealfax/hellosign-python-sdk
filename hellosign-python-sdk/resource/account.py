from http.http_post_request import HttpPostRequest
from http.http_get_request import HttpGetRequest
from resource import Resource

class Account(Resource):

	ACCOUNT_KEY = "account";
	ACCOUNT_ID = "account_id";
	ACCOUNT_EMAIL_ADDRESS = "email_address";
	ACCOUNT_IS_PAID_HS = "is_paid_hs";
	ACCOUNT_IS_PAID_HF = "is_paid_hf";
	ACCOUNT_TEMPLATES_LEFT = "templates_left";
	ACCOUNT_API_SIG_REQS_LEFT = "api_signature_requests_left";
	ACCOUNT_CALLBACK_URL = "callback_url";
	ACCOUNT_ROLE_CODE = "role_code";
	OAUTH_DATA = "oauth_data";
	ACCOUNT_PASSWORD = "password";

	"""docstring for Account"""
	# def __init__(self, arg):
	# 	super(Account, self).__init__()
	# 	self.arg = arg

	def create(self, email, password):
		# TODO: 
		if email is None:
			print ("Email is not valid")
		if password is None:
			print ("Password is not valid")
		get_request = HttpPostRequest()
		response = get_request.post('https://api.hellosign.com/v3/account/create', {'email_address': email, 'password': password})
		return response

	def get_info(self):
		get_request = HttpGetRequest()
		response = get_request.get_json_response('https://api.hellosign.com/v3/account')
		return response

	def update_info(self):
		get_request = HttpGetRequest()
		response = get_request.get_json_response('https://api.hellosign.com/v3/account')
		return response