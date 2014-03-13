# from http.http_get_request import HttpGetRequest
from http.http_post_request import HttpPostRequest
from resource.account import Account

# get_request = HttpGetRequest()
post_request = HttpPostRequest()
# print get_request.get_json_response('https://github.com/timeline.json')
# print get_request.get_file_response('https://github.com/timeline.json', 'testfile.json')
account = Account()
# print account.create('minhdanh72@gmail.com', 'testabcd094')
print account.get_info()
