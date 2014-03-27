from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.resource.team import Team
from hellosign_python_sdk.resource.reusable_form import ReusableForm
from hellosign_python_sdk.utils.exception import Forbidden


class TestReusableForm(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_resuable_form(self):
        # Get reusable form list, if there's any:
        # Add a user to our team, get the first one
        # if no team exist, create team
        # then add and remove a user from/to this reusableform
        # remove user from our team
        # destroy team
        rfl = self.client.get_reusable_form_list()
        self.assertTrue(isinstance(rfl, list))
        create_team = False
        if len(rfl) > 0:
            self.assertTrue(isinstance(rfl[0], ReusableForm))

            try:
                team = self.client.get_team_info()
            except Forbidden:
                team = self.client.create_team("Team Name")
                self.assertTrue(isinstance(team, Team))
                self.assertEquals(team.name, "Team Name")
                create_team = True
            try:
                new_team = self.client.add_team_member("test_user_hs@example.com")
                self.assertTrue(isinstance(new_team, Team))
                print [account["email_address"] for account in team.accounts]
                self.assertTrue("test_user_hs@example" in [account["email_address"] for account in team.accounts])
                if "test_user_hs@example" in [account["email_address"] for account in team.accounts]:
                    rf = self.client.get_reusable_form(rfl[0].reusable_form_id)
                    self.assertTrue(isinstance(rf, ReusableForm))

                    rf = self.client.add_user_to_reusable_form(
                        rfl[0].reusable_form_id, None, "test_user_hs@example.com")
                    self.assertTrue(isinstance(rf, ReusableForm))

                    rf = self.client.remove_user_from_reusable_form(
                        rfl[0].reusable_form_id, None, "test_user_hs@example.com")
                    self.assertTrue(isinstance(rf, ReusableForm))

                new_team = self.client.remove_team_member("test_user_hs@example.com")
                self.assertTrue(isinstance(team, Team))
                self.assertFalse("test_user_hs@example" in [account["email_address"] for account in team.accounts])

            except Forbidden:
                pass
            if create_team is True:
                result = self.client.destroy_team()
                self.assertTrue(result)