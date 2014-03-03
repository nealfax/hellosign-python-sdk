from hsclient import HSClient

client = HSClient()
# Account
# client.get_account_info()
# print client.account.email_address # print minhdanh@siliconstraits.vn
# client.account.callback_url = "http://git.siliconstraits.vn"
# client.update_account_info()
# client.get_account_info()
# print client.account.callback_url # print http://git.siliconstraits.vn
# print client.account.documents_left # print 3
# print client.account.email_address # print minhdanh@siliconstraits.vn

# SignatureRequest
# client.create_account("tranthienthanh@gmail.com", "abczyxll00348")
client.get_signature_request_list()