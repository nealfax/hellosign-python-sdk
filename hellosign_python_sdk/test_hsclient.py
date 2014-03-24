from hsclient import HSClient
from utils.hsaccesstokenauth import HSAccessTokenAuth
# from hellosign_python_sdk.resource.unclaimed_draft import UnclaimedDraft


client = HSClient(api_key="a57f10309a04482499e49782b3c0c6f43641780970c2c1d02451c74b03ece07c")
# Account
# client.get_account_info()
# print client.account.email_address # print minhdanh@siliconstraits.vn
# client.account.callback_url = "http://git.siliconstraits.vn"
# client.update_account_info()
# client.get_account_info()
# print client.account.callback_url # print http://git.siliconstraits.vn
# print client.account.documents_left # print 3
# print client.account.email_address # print minhdanh@siliconstraits.vn
# print client.account

# SignatureRequest
# print client.create_account("tranthienthanh@gmail.com.vn", "abczyxll00348")
# client.create_account("@gmail.com", "abczyxll00348") # invalidemail
# sr = client.get_signature_request("7bf722477992c7fe445da9b46b71fd7a53885fab")
# print sr.requester_email_address  # o0Khoiclub0o@yahoo.com`
# sr_list = client.get_signature_request_list()
# print sr_list  # True
# print sr_list[0]  # True
# print sr_list[0].signatures[0]['signer_name']  # True
# download file
# client.get_signature_request_file("7bf722477992c7fe445da9b46b71fd7a53885fab", "file.pdf") # file.pdf
# client.get_signature_request_final_copy("7bf722477992c7fe445da9b46b71fd7a53885fab", "file2.pdf") # file.pdf
# rf_list = client.get_reusable_form_list()
# print rf_list[0].reusable_form_id # print 85185eeafa15704ce7be1a9d5e911c2366f5313e
# 4
# rf = client.get_reusable_form("85185eeafa15704ce7be1a9d5e911c2366f5313e")
# print rf.signer_roles[0]['name']
# 5
# a = client.get_team_info()
# print a.accounts
# 6
# client.create_team("SSS Dev Team")
# 7
# 400 Could not update, none exists. if no team created yet
# client.update_team_name("SSS HelloSign Dev Team")
# 8
# client.destroy_team()
# # 9
# print client.add_team_member("dinhkhoi@siliconstraits.vn") # ok
# client.add_team_member("anhduy@siliconstraits.vn") # ok
# 10
# print client.add_team_member("anhduy@siliconstraits.vn") # error
# 11
# print client.remove_team_member("anhduy@siliconstraits.vn")
# print client.remove_team_member("dinhkhoi@siliconstraits.vn")
# print client.remove_team_member("xysdfksdf@siliconstraits.vn")

# # 12
# files = ["/Users/minhdanh/Downloads/aws-sdk-ruby-dg.pdf", "/Users/minhdanh/Downloads/Hadoop_Tuning_Guide-Version5.pdf"]
# files = ["/Users/minhdanh/Downloads/aws-sdk-ruby-dg.pdf"]
# signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}]
# signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}, {"name": "Vo Anh Duy", "email_address": "anhduy@siliconstraits.vn"}, {"name": "Minh Danh", "email_address": "minhdanh@siliconstraits.vn"}]
# cc_email_addresses = ["anhduy@siliconstraits.vn", "minhdanh@siliconstraits.vn"]

# print client.send_signature_request("1", "", ["http://www.ancestralauthor.com/download/sample.pdf"], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses)
# print client.send_signature_request("1", files, ["http://www.ancestralauthor.com/download/sample.pdf"], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses)
# print client.send_signature_request("1", files, [], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses)
# print client.send_signature_request("1", None, [], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses) # Error
# 13 TODO: test create with reusable_form_id
# signers = [{'email_address': 'minhdanh@tgm.vn',
#   'name': 'Minh Danh',
#   'role_name': 'Ben Thang Cuoc'},
#  {'email_address': 'anhduy@siliconstraits.vn',
#   'name': 'Anh Duy',
#   'role_name': 'Ben Thua Cuoc'}]
# ccs = [{'email_address': '', 'role_name': 'US President'},
#  {'email_address': 'dinhkhoi@siliconstraits.vn', 'role_name': 'UN'}]
# custom_fields = [{"Client's name": 'None'}, {'He he': 'None'}]
# sr = client.send_signature_request_embedded_with_rf(test_mode = "1",
#                 client_id = '6a8949c799991e12dac70cb135095680', reusable_form_id = '795d750e70f1bb2146541022bdec3b1b0ac5ae0c', title = "NDA with Acme Co.",
#                 subject = "The NDA we talked about", message = "Please sign this NDA and then we" +
#                 " can discuss more. Let me know if you have any questions.",
#                 signing_redirect_url = "", signers = signers, ccs = ccs, custom_fields = custom_fields)
# print sr.signatures[0]["signature_id"]
#14 reminder
# client.remind_signature_request("ba9e7d19133c9a369ee35bafb1bb23942580994e", "minhdanh@siliconstraits.vn")
#15 cancel
# client.cancel_signature_request("ba9e7d19133c9a369ee35bafb1bb23942580994e")
# 16

# files = ["/Users/minhdanh/Downloads/aws-sdk-ruby-dg.pdf", "/Users/minhdanh/Downloads/Hadoop_Tuning_Guide-Version5.pdf"]
# files = ["/Users/minhdanh/Downloads/aws-sdk-ruby-dg.pdf"]
# signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}]
# signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}, {"name": "Vo Anh Duy", "email_address": "anhduy@siliconstraits.vn"}, {"name": "Minh Danh", "email_address": "minhdanh@siliconstraits.vn"}]
# cc_email_addresses = ["anhduy@siliconstraits.vn", "minhdanh@siliconstraits.vn"]
# # TODO: use a valid client_id
# print client.send_signature_request_embedded("1", "6a8949c799991e12dac70cb135095680", files, [], "Test create signature request", "Ky giay no", "Ky vao giay no di, le di", "", signers, cc_email_addresses)
# 17 TODO: test create with reusable_form_id

# Test ReusableForm
#18
# rl = client.get_reusable_form_list()
# for rf in rl:
# 	print rf.json_data
# 19 get reusable_form_id
# rf = client.get_reusable_form("85185eeafa15704ce7be1a9d5e911c2366f5313e")
# print rf.reusable_form_id
# 20
# print client.add_user_to_reusable_form("85185eeafa15704ce7be1a9d5e911c2366f5313e", email_address="dinhkhoi@siliconstraits.vn").reusable_form_id
# print client.remove_user_from_reusable_form("85185eeafa15704ce7be1a9d5e911c2366f5313e", email_address="dinhkhoi@siliconstraits.vn")

# Test UnclaimedDraft
# 21

# files = ["/Users/minhdanh/Downloads/aws-sdk-ruby-dg.pdf", "/Users/minhdanh/Downloads/Hadoop_Tuning_Guide-Version5.pdf"]
# # signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}]
# signers = [{"name": "Vu Dinh Khoi", "email_address": "dinhkhoi@siliconstraits.vn"}, {"name": "Vo Anh Duy", "email_address": "anhduy@siliconstraits.vn"}, {"name": "Minh Danh", "email_address": "minhdanh@siliconstraits.vn"}]
# cc_email_addresses = ["anhduy@siliconstraits.vn", "minhdanh@siliconstraits.vn"]

# a = client.create_unclaimed_draft("1", files, [], UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE , "Test unclaimed draft", "Please do not reploy to the messages", signers, cc_email_addresses)
# print a.claim_url

# Test oauth

a =  client.get_oauth_data("369c76ae6185f3b7", "6a8949c799991e12dac70cb135095680", "a97d141f743a64e598d4baebdf18dc7a", "demo")
oauth = HSAccessTokenAuth(a['access_token'], a['token_type'], a['refresh_token'], a['expires_in'], a['state'])
print oauth