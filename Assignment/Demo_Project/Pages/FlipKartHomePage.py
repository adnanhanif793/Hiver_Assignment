
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class FlipKartHomePage:

    def __init__(self, driver):
        self.driver = driver


    def clickByXpath(self,locator):
        self.driver.find_element_by_xpath(locator).click()

    def moveToElement(self,locator):
        element = self.driver.find_element_by_xpath(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def switchWindow(self):

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)


    def getAmount(self,locator):
        price = self.driver.find_element_by_xpath(locator).text
        amount = price.split('₹')
        print("Flipkart price is :Rs",amount[1])
        return amount[1]

    def searchItem(self,locator,text):
        item=self.driver.find_element_by_xpath(locator)
        item.send_keys(text,Keys.RETURN)

