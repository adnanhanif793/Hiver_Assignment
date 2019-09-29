from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Assignment.Demo_Project.Pages.FlipKartHomePage import FlipKartHomePage
from Assignment.Demo_Project.Locators.FlipKartLocators import FlipKartLocator



class Flipkart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.flipkart.com")
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath("//span[text()='Enter Email/Mobile number']/ancestor::div/button").click()

    def test_flipkartScenario(self):

        Fhomepage=FlipKartHomePage(self.driver)
        Fhomepage.moveToElement(FlipKartLocator.Electronics_Menu_xpath)
        Fhomepage.clickByXpath(FlipKartLocator.Pixel3a_SubMenu_xpath)
        Fhomepage.clickByXpath(FlipKartLocator.FirstPhone_xpath)
        Fhomepage.switchWindow()
        Fhomepage.clickByXpath(FlipKartLocator.AddTOCart_Button_xpath)
        time.sleep(3)
        Fhomepage.clickByXpath(FlipKartLocator.AddQuantity_Button_xpath)
        time.sleep(2)
        Fhomepage.getAmount(FlipKartLocator.TotalAmount_Text_xpath)




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
