import os
import unittest

import weblogin
# import selenimum

class WebLoginTest(unittest.TestCase):
    pwd = os.getcwd()

    def setUp(self):
        url = 'file:/' + self.pwd + '/Login-Spotify.html'
        print("Set test webpage at:" + url)
        self._testweb = weblogin.WebLogin()
        self._testweb.launch(website=url, showGUI=False)

    def test_1_find_field(self):
        self._testweb.find_input()
        # pass

    def test_2_login(self):
        self._testweb.send_keys()
        
    def tearDown(self):
        if self._testweb:
            del self._testweb

class WebLoginNotFindTest(unittest.TestCase):
    def setUp(self):
        url = 'file:/' + self.pwd + '/Login-Spotify2.html'
        print("Set test webpage at:" + url)
        self._testweb = weblogin.WebLogin()
        self._testweb.launch(website=url, showGUI=False)

    def test_1_not_find(self):
        self._testweb.find_input()

    def tearDown(self):
        if self._testweb:
            del self._testweb


if __name__ == '__main__':
    unittest.main()
