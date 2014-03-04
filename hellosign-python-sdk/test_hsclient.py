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
#sr = client.get_signature_request("7bf722477992c7fe445da9b46b71fd7a53885fab")
#print sr.requester_email_address  # o0Khoiclub0o@yahoo.com`
#sr_list = client.get_signature_request_list()
#print sr_list[0].test_mode  # True
# download file
# client.get_signature_request_file("7bf722477992c7fe445da9b46b71fd7a53885fab", "file.pdf") # file.pdf
# client.get_signature_request_final_copy("7bf722477992c7fe445da9b46b71fd7a53885fab", "file2.pdf") # file.pdf
