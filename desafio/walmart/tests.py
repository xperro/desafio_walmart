from django.test import TestCase

# Create your tests here.

# Create your tests here.
from . import helpers


class CheckPalindromeFunction(TestCase):

    @classmethod
    def setUp(self):
        self.test1 = 181
        self.test2 = "asa"
        self.test3 = "assa"
        self.test4 = ""
        self.test5 = 18

    def test_palindrome1(self):
        print("Test palindrome 181")
        response = helpers.CheckPalindrome(str(self.test1))
        self.assertTrue(response, True)

    def test_palindrome2(self):
        print("Test palindrome asa")
        response = helpers.CheckPalindrome(str(self.test2))
        self.assertTrue(response, True)

    def test_palindrome3(self):
        print("Test palindrome assa")
        response = helpers.CheckPalindrome(str(self.test3))
        self.assertTrue(response, True)

    def test_palindrome4(self):
        print("Test palindrome '' ")
        response = helpers.CheckPalindrome(str(self.test4))
        self.assertFalse(response, False)

    def test_palindrome5(self):
        print("Test palindrome 18")
        response = helpers.CheckPalindrome(str(self.test5))
        self.assertFalse(response, False)

    def test_discount(self):
        print("Test 50% off")
        response = helpers.discount(1000)
        self.assertEquals(response, 500)

    def test_connection(self):
        print("Test connection mongodb")
        state = helpers.connect()
        self.assertTrue(state, False)

    def test_integration(self):
        print("Test integration case 1")
        while helpers.connect() == False:
            print("Waiting for mongodb connection")
        test1 = helpers.integration_test_function(self.test1)
        palindrome = helpers.CheckPalindrome(str(self.test1))

        for product in test1:
            self.assertEquals(product["id"], 181)
            self.assertEquals(palindrome, True)

    def test_integration2(self):
        print("Test integration case 2")
        while helpers.connect() == False:
            print("Waiting for mongodb connection")
        test2 = helpers.integration_test_function(self.test2)
        palindrome = helpers.CheckPalindrome(self.test2)
        condition = False
        if len(self.test2) > 3:
            condition = True
        self.assertEquals(palindrome, True)
        self.assertEquals(len(test2), 8)
        self.assertEquals(condition, False)

    def test_integration3(self):
        print("Test integration case 3")
        while helpers.connect() == False:
            print("Waiting for mongodb connection")
        test3 = helpers.integration_test_function(self.test3)
        palindrome = helpers.CheckPalindrome(self.test3)
        condition = False
        if len(self.test2) > 3:
            condition = True
        for product in test3:
            self.assertEquals(palindrome, True)
            self.assertEquals(len(test3), 35)
            self.assertEquals(condition, False)

    def test_integration4(self):
        print("Test integration case 4")
        while helpers.connect() == False:
            print("Waiting for mongodb connection")
        test4 = helpers.integration_test_function(self.test5)
        while test4 == '':
            print("Retry...")
        palindrome = helpers.CheckPalindrome(str(self.test5))
        condition = False
        for product in test4:
            self.assertEquals(palindrome, False)
            self.assertEquals(len(test4), 1)