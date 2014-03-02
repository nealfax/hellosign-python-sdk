from http.request import HSRequest
from resource.account import Account
from hsclient import HSClient

request = HSRequest()
account = Account()
client = HSClient()
# Test get function
# print request.get('https://github.com/timeline.json')
# Test request through account's get_info
# print account.get_info()
# Test request post
# print client.create_account('minhdanh72@yahoo.com', 'testabcd094')
# 4
account = Account(key="account")
a = Account(account.get_info(), "account")
# print a.email_address # print minhdanh@siliconstraits.vn
# a.email_address = "minhdanh72@gmail.com"
# print a.email_address #print minhdanh72@gmail.com
# print a.email # raise AttributeError
# print a.is_paid_hs # False
print a.quotas["templates_left"] # TODO: use a more natural way like a.quotas.templates_left here
print a.json_data # json object


