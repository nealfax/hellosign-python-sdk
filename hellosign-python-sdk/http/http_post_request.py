import os
import requests
import json
import tempfile

class HttpPostRequest(object):

	# TODO: implement from an abstract class for post & get
	DEFAULT_ENCODING = "UTF-8";
	USER_AGENT = "HelloSign Java SDK";
	url = ""
	parameters = {}
	headers = {'User-Agent': USER_AGENT}
	API_USER = "minhdanh@siliconstraits.vn"
	API_PASSWORD = "miCSnwVp2qkZa73WjE"

	def get_json_response(self, url):
		response = requests.get(url, headers=self.headers)
		response.encoding = self.DEFAULT_ENCODING
		if response.status_code == 200:
			return response.json()

	def post(self, url, data):
		response = requests.post(url, headers=self.headers, data=data, auth=(self.API_USER, self.API_PASSWORD))
		if response.status_code == 200:
			return response.json()
		else:
			return response.text