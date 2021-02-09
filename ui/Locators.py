from selenium.webdriver.common.by import By


class Locators:
    #home page locators:
    Weather = "//div[@class='topnav_cont']//a[contains(text(), 'WEATHER')]"
    topNav = "//div[@class='neweleccont ntopnav_wrap2']"

    #Weather page locators:
    cityTempInfoPopup = "//div[contains(@class, 'leaflet-popup-content-wrapper')]//span[4]/b"
    cityHumidityInfoPopup = "//div[contains(@class, 'leaflet-popup-content-wrapper')]//span[3]/b"
    citySelector = "//div[@class='comment_cont']"
    mapCanvas = "//*[@id='map_canvas']"

    parentConvas1 = "//div[@class='leaflet-pane leaflet-map-pane']"
    parentConvas2 = "//div[@class='leaflet-pane leaflet-marker-pane']"


class POM:

    def __init__(self, driver):
        self.driver = driver

        self.Weather = driver.find_element(By.XPATH, Locators.Weather)
        self.topNav = driver.find_element(By.XPATH, Locators.topNav)
        self.cityTempInfoPopup = driver.find_element(By.XPATH, Locators.cityTempInfoPopup)
        self.cityHumidityInfoPopup = driver.find_element(By.XPATH, Locators.cityHumidityInfoPopup)
        self.citySelector = driver.find_element(By.XPATH, Locators.citySelector)
        self.mapCanvas = driver.find_element(By.XPATH, Locators.mapCanvas)

        self.parentConvas1 = driver.find_element(By.XPATH, Locators.parentConvas1)
        self.parentConvas2 = driver.find_element(By.XPATH, Locators.parentConvas2)
