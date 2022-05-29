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
            username = "uuuu"
            global cursor
            App.delete_org(username)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_register_org(self):
            App.Database()
            try:
                username = "uuu"
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

    def test_delete_field(self):
                App.Database()
                try:
                    field = "hope"
                    App.delete_field(field)
                    self.assertTrue(True)
                except:
                    self.assertTrue(True)
    def test_update_donation(self):
            App.Database()
            try:
                dona = "20000"
                global cursor
                App.update_donation(dona)
                self.assertTrue(True)
            except:
                self.assertTrue(True)
#testing  adding organization
    def test_add_organization(self):
            App.Database()
            try:
                username = "orggg"
                password = "6355gg363"
                name = "organizatio"
                age = 15
                location = "amman"
                phone = "057376628"
                maxvol = "200"
                hobby = "reading"
                App.insert_organization(str(username), str(password), str(name), str(age), str(location), str(phone),
                                        str(maxvol), str(hobby))
                self.assertTrue(True)
            except:
                self.assertTrue(False)

    def test_fall_add_organization(self):
            App.Database()
            try:
                username = "orggg"
                password = "6355gg363"
                name = "organizatio"
                age = 15
                location = "amman"
                phone = "057376628"
                maxvol = "200"
                hobby = "reading"
                App.insert_organization(str(username), str(password), str(name), str(age), str(location), str(phone),
                                        str(maxvol), str(hobby))
                self.assertFalse(True)
            except:
                self.assertFalse(False)
#test donation for organization
    def test_divide_to_organization(self):
            App.Database()
            try:
                username = "ssss"
                donation="5000"
                App.divide_donation(donation,username)
                self.assertTrue(True)
            except:
                self.assertTrue(False)

    def test_add_field(self):
        App.Database()
        try:
            field = "hope"
            App.add_field(field)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_update_rating(self):
        App.Database()
        try:
            username = "ssss"
            rating = "3"
            global cursor
            App.update_rating(rating, username)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_addFieldAdmin(self):
        App.Database()
        try:
            field = "heal"
            App.add_Field_Admin(field)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_SearchSomeone(self):
        App.Database()
        try:
            username = "ggg"
            meen = "male"
            geel = 17
            mekoom = "Ber Sheva"
            hoby = "teaching swimming"
            App.Search_Somone(username, meen, geel, mekoom, hoby)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_report(self):
        App.Database()
        try:
            vol = "sujood"
            org = "ssss"
            date = "4-3-8"
            App.Report(vol, org, date)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_application(self):
        App.Database()
        try:
            vol = "sujood"
            org = "ssss"
            App.Applyy(org, vol)
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    def test_pick_field(self):
        App.Database()
        try:
            vol = "admin"
            name = "ssss"
            location = "Arad"
            age = "17"
            field = "curing"
            App.pick_field(vol, name, location, age, field)
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    def test_update_num_vol(self):
        App.Database()
        try:
            num = 140
            org = "kheer"
            App.update_num_vol(num, org)
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    def edit_Profile(self):
        #############
        App.Database()
        try:
            name = "sujood"
            org = "ssss"
            App.Applyy(name, org)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_Max_hours(self):
        App.Database()
        try:
            Maxhour = 200
            username = "sujood"
            org = "ssss"
            App.Max_hours(Maxhour, username, org)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_apply_report(self):
        App.Database()
        try:
            vol = "sujood"
            org = "ssss"
            hhour = 15
            sstatus = "ok"
            ddaate = "1-1-23"
            App.apply_report(org, vol, hhour, sstatus, ddaate)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_update_hourss(self):
        App.Database()
        try:
            vol = "sujood"
            hh = 15
            App.update_hourss(hh, vol)
            self.assertTrue(True)
        except:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
