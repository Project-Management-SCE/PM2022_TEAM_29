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
            username = "sondoss"
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
    def test_delete(self):
        App.Database()
        try:
            username = "sujood"
            global cursor
            App.delete(username)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_delete_organization(self):
        App.Database()
        try:
            username = "ssss"
            global cursor
            App.delete_org(username)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_register_org(self):
            App.Database()
            try:
                username = "kkk"
                password = "78337363"
                name = "arina"
                age = 19
                location = "saudi"
                phone = "0537352882"
                maxvol = "150"
                hobby = "curing"
                App.insert_organization(str(username), str(password), str(name), str(age), str(location), str(phone),
                                    str(maxvol), str(hobby))
                self.assertTrue(True)
            except:
                self.assertTrue(False)
    def test_fall_register(self):
            App.Database()
            try:
                username = "kuuu"
                password = "78337363"
                name = "arina"
                age = 19
                location = "saudi"
                phone = "0537352882"
                maxvol = 150
                hobby = "curing"
                App.insert_organization(str(username), str(password), str(name), str(age), str(location), str(phone),
                                        str(maxvol), str(hobby))
                self.assertFalse(True)
            except:
                self.assertFalse(False)

    def delete_field(f):
        Database()
        global cursor
        cursor.execute("DELETE FROM 'organization' WHERE hobby=?", (f,))
        conn.commit()


if __name__ == '__main__':
    unittest.main()
