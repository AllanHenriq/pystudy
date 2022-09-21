from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class drivers:

    def loadDriver(driver):
        if driver=="edge":
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            print(driver + "is not a valid driver")

        return driver