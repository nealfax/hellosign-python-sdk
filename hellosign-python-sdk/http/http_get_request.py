import os
import requests
import json
import tempfile

class HttpGetRequest(object):

	DEFAULT_ENCODING = "UTF-8";
	USER_AGENT = "HelloSign Java SDK";
	url = ""
	parameters = {}
	headers = {'User-Agent': USER_AGENT}
	API_USER = "minhdanh@siliconstraits.vn"
	API_PASSWORD = "miCSnwVp2qkZa73WjE"

	def get_json_response(self, url):
		response = requests.get(url, headers=self.headers, auth=(self.API_USER, self.API_PASSWORD))
		response.encoding = self.DEFAULT_ENCODING
		if response.status_code == 200:
			return response.json()
		else:
			return response.text


	def get_file_response(self, url, filename):
		try:
			temp = open(filename, 'w+b')
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
		response = requests.get(url, headers=self.headers)
		response.encoding = self.DEFAULT_ENCODING
		if response.status_code == 200:
			temp.write(response.content)
			temp.close()
			return temp