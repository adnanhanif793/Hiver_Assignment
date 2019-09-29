from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class AmazonHomePage:

    def __init__(self, driver):
        self.driver = driver

    def openFlipkart(self):
        self.driver.get("https://www.flipkart.com")
        self.driver.find_element_by_xpath("//span[text()='Enter Email/Mobile number']/ancestor::div/button").click()

    def clickByXpath(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def searchItem(self,locator,text):
        item=self.driver.find_element_by_xpath(locator)
        item.send_keys(text,Keys.RETURN)



    def moveToElement(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(4)

    def closeWindow(self):
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])


    def comparePrice(self,Aprice,Fprice):
        self.Aprice=Aprice
        self.Fprice=Fprice
        if(Aprice>Fprice):
            print("Flipkart price is less:",Fprice)
        elif(Aprice<Fprice):
            print("Amazon price is less:", Aprice)

        else:
            print("Both price are equal", Aprice)


    def getAmountAm(self, locator):
        price = self.driver.find_element_by_xpath(locator).text
        amount = price.split(' ')
        print("Amazon Price:Rs",amount[1])
        return amount[1]
