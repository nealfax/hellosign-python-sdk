from unittest import TestCase
from hellosign.utils.utils import *


class TestUtils(TestCase):

    def test_check_email(self):
        self.assertEqual(is_email("test@test.com"), True)
        self.assertEqual(is_email("test@test.com.vn"), True)
        self.assertEqual(is_email("user_test@test.com"), True)
        self.assertEqual(is_email("user.test@test.com"), True)
        self.assertEqual(is_email("a.little.lengthy.but.fine@dept.example.com"),
                         True)
        self.assertEqual(is_email("other.email-with-dash@example.com"), True)
        self.assertEqual(is_email("long_long_long_long_test@test.com"), True)
        self.assertEqual(is_email("@test.com"), False)
        self.assertEqual(is_email("test@test"), False)
        self.assertEqual(is_email("test@test_com"), False)
        self.assertEqual(is_email("test @test.com"), False)
        self.assertEqual(is_email("testcom"), False)
        self.assertEqual(is_email("test.com"), False)
        self.assertEqual(is_email(""), False)
        self.assertEqual(is_email("test"), False)
        self.assertEqual(is_email("A@b@c@example.com"), False)
        self.assertEqual(is_email("a\"b(c)d,e:f;g<h>i[j\k]l@example.com"),
                         False)
        self.assertEqual(is_email("just\"not\"right@example.com"), False)
        self.assertEqual(is_email("this is\"not\\allowed@example.com"), False)
        self.assertEqual(is_email("this\ still\"not\\allowed@example.com"),
                         False)
