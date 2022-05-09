import unittest
from flask import app
from flask_wtf import form
import App


class MyTestCase(unittest.TestCase):
    def test_register(self):
        App.Database()
        try:
            username = "sujood"
            password = "123445"
            name = "sama"
            age = 23
            location = "arad"
            phone = "0433433443"
            hour = 15
            hobby = "reading and helping people"
            App.insert_volunteer(str(username), str(password), str(name), str(age), str(location), str(phone), str(hobby))
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def test_fall_register(self):
        App.Database()
        try:
            username = "sujood"
            password = "123445"
            name = "sama"
            age = 23
            location = "arad"
            phone = "0433433443"
            hour = 15
            hobby = "reading and helping people"
            App.insert_volunteer(str(username), str(password), str(name), str(age), str(location), str(phone), str(hobby))
            self.assertFalse(True)
        except:
            self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
