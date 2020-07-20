import unittest
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonAuthMoudle(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def readData(self):
        with open('data.json') as data:
            user_data = json.load(data)
        return user_data
    
    def auth_alg(self, event):
        driver = webdriver.Chrome()
        data = self.readData()
        driver.get(data.get("url"))
        login = driver.find_element_by_name("login")
        login.send_keys(data[event]["login"])
        password = driver.find_element_by_name("password")
        password.send_keys(data[event]["password"])
        password.send_keys(Keys.RETURN)

        if (event == 'error'):
            self.assertTrue(driver.find_element_by_name("login"))
        else:
            self.assertTrue(driver.find_element_by_id("map"))

        driver.close()

    def test_auth_success(self):
        self.auth_alg('success')
        
    def test_auth_error(self):
        self.auth_alg('error')
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()