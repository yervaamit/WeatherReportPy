from ui.Locators import Locators
from configparser import ConfigParser
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest


class NDTVWeatherInfo:

    def __init__(self, driver, driver_wait):
        self.driver = driver
        self.driver_wait = driver_wait

    def ndtv_weather_data(self):
        city = get_config_value('WeatherInfo', 'city')
        self.driver.execute_script(
            "arguments[0].setAttribute('style', 'position: static; padding-top: 0px; display: block;')",
            self.driver.find_element(By.XPATH, Locators.topNav))
        self.driver.find_element(By.XPATH, Locators.Weather).click()
        self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.parentConvas1)))
        self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.parentConvas2)))
        print("Element turned out to be clickable")

        if self.is_city_selected(city) is None:
            self.driver.find_element(By.XPATH, "//label[@for='" + city + "']/input").click()

        self.driver.find_element(By.XPATH, "//div[@title='" + city + "']").click()
        self.driver_wait.until(EC.element_to_be_clickable((By.XPATH, Locators.cityTempInfoPopup)))
        web_temp = self.driver.find_element_by_xpath(Locators.cityTempInfoPopup).text
        temperature = web_temp.split(':')[1].strip()
        print(f"Text from webElement :  {web_temp}. Temperature in degree :  {temperature}")
        return temperature

    def api_weather_data(self):
        query_params = {'q': get_config_value('WeatherInfo', 'city'), 'AppId': get_config_value('API', 'AppId')}
        response = requests.post(get_config_value('API', 'BaseURL'), params=query_params)
        if response.status_code == 200:
            try:
                jsonResp = response.json()
            except Exception:
                print("Exception while parsing response JSON")
        else:
            return

        temper = jsonResp.get('main').get('temp') - 273.15
        print(f"Temperature of Response received from the API : {temper}")
        return temper

    def is_city_selected(self, city):
        try:
            var = self.driver.find_element(By.XPATH, "//label[@for='" + city + "']/input").get_attribute("checked")
            return var
        except BaseException:
            return


def get_config_value(section, key):
    parser = ConfigParser()
    parser.read(r"/Users/amityerva/PycharmProjects/SeleniumAPI/Parameters.ini")
    return parser.get(section, key)


if __name__ == '__main__':
    unittest.main()
