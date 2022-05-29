import unittest
import unittest
from flask import app
from flask_wtf import form
from App import app
import json
import App


class TestHello(unittest.TestCase):
    # User login with correct details
    def setUp(self):
        App.testing = True
        self.app = App.test_client()

    def test_homePage(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_login_logout(self):
        taster = App.test_client(self)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        self.assertTrue(rv.status, '200 OK')
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv = taster.get('/logout', follow_redirects=True)
        self.assertFalse('התנתקת בהצלחה'.encode() in rv.data)

    def test_login_session(self):
        taster = App.test_client(self)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.get('/login', follow_redirects=True)
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv = taster.get('/logout', follow_redirects=True)

    def test_delete_user(self):
        taster = App.test_client(self)
        rv = taster.post('/register', data=dict(username="sujood", password="123445", name="test", last="test"),
                         follow_redirects=True)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.post('/unregister', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        self.assertFalse('שם משתמש או סיסמא לא נכונים'.encode() in rv.data)

    def test_comment(self):
        taster = App.test_client(self)
        rv = taster.post('/register', data=dict(username="sujood", password="123445", name="test", last="test"),
                         follow_redirects=True)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.post('/comments/פארק%20ליכטנשטיין', data=dict(comment="test"), follow_redirects=True)
        rv = taster.get('/comments/פארק%20ליכטנשטיין')
        self.assertFalse('test'.encode() in rv.data)
        rv = taster.post('/unregister', data=dict(username="sujood", password="123445"), follow_redirects=True)

    def test_login_as_admin(self):
        taster = App.test_client(self)
        rv = taster.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        rv = taster.get('/login', follow_redirects=True)
        rv = taster.get('/logout', follow_redirects=True)
        self.assertFalse('test'.encode() in rv.data)

    def test_login_as_visit(self):
        taster = App.test_client(self)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.get('/login', follow_redirects=True)
        self.assertFalse('משתמשים'.encode() in rv.data)
        rv = taster.get('/logout', follow_redirects=True)

    def test_add_admin(self):
        taster = App.test_client(self)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        rv = taster.get('/login', follow_redirects=True)
        rv = taster.post('/registerByAdmin',
                         data=dict(name="טסט", last="טסט", username="sujood", password="123445", Admin="true"),
                         follow_redirects=True)
        rv = taster.get('/logout', follow_redirects=True)
        rv = taster.post('/login', data=dict(username="sujood", password="123445"), follow_redirects=True)
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv = taster.post('/unregister', data=dict(username="sujood", password="123445"), follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
