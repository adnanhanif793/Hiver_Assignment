from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Assignment.Demo_Project.Pages.FlipKartHomePage import FlipKartHomePage
from Assignment.Demo_Project.Locators.FlipKartLocators import FlipKartLocator
from Assignment.Demo_Project.Pages.AmazonHomePage import AmazonHomePage
from Assignment.Demo_Project.Locators.AmazonLocators import AmazonLocator


class Amazon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.amazon.in")
        cls.driver.maximize_window()

        #cls.driver.find_element_by_xpath("//span[text()='Enter Email/Mobile number']/ancestor::div/button").click()

    def test_amazonScenario(self):

        Ahomepage=AmazonHomePage(self.driver)
        Fhompage=FlipKartHomePage(self.driver)
        Ahomepage.searchItem(AmazonLocator.SearchBox_xpath,"iphone xr 128 gb(black)")
        Ahomepage.clickByXpath(AmazonLocator.iPhoneXR_xpath)
        Ahomepage.switchWindow()
        Aprice=Ahomepage.getAmountAm(AmazonLocator.iPhonePrice_id)
        Ahomepage.closeWindow()
        Ahomepage.openFlipkart()

        Fhompage.searchItem(FlipKartLocator.SearchBox_xpath,"iphone xr 128 gb(black)")
        Fhompage.clickByXpath(FlipKartLocator.iPhoneXR_xpath)
        Fhompage.switchWindow()
        Fprice=Fhompage.getAmount(FlipKartLocator.iPhonePrice_xpath)
        Ahomepage.comparePrice(Aprice,Fprice)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
