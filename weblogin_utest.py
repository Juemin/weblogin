import os
import unittest

import weblogin
# import selenimum

pwd = os.getcwd()

class WebLoginTest(unittest.TestCase):
    testweb = None
    
    @classmethod
    def setUpClass(cls):
        url = 'file:/' + pwd + '/Login-Spotify.html'
        print("Set test webpage at:" + url)
        cls.testweb = weblogin.WebLogin()
        cls.testweb.launch(website=url, showGUI=False)
    
    @classmethod
    def tearDownClass(cls):
        if cls.testweb:
            del cls.testweb

    def test_1_find_field(self):
        self.testweb.find_input()

    def test_2_login(self):
        self.testweb.send_keys()


class WebLoginNotFindTest(unittest.TestCase):
    testweb = None
    
    @classmethod
    def setUpClass(cls):
        url = 'file:/' + pwd + '/Login-Spotify2.html'
        print("Set test webpage at:" + url)
        cls.testweb = weblogin.WebLogin()
        cls.testweb.launch(website=url, showGUI=False)

    @classmethod
    def tearDown(cls):
        if cls.testweb:
            del cls.testweb

    def test_1_not_find(self):
        # self._testweb.find_input()
        pass


if __name__ == '__main__':
    unittest.main()
