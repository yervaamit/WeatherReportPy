from ui.BaseTest import BaseTest
from ui.NDTVWeatherPage import NDTVWeatherInfo
from ui.NDTVWeatherPage import get_config_value


class ValidateTemperature(BaseTest):

    def test_city_temperature(self):
        driver = self.driver
        driver_wait = self.webDriverWait
        weather_info = NDTVWeatherInfo(driver, driver_wait)
        ndtv_data = round(float(weather_info.ndtv_weather_data()), 2)
        api_data = weather_info.api_weather_data()
        if api_data is not None and ndtv_data is not None:
            variance_perc = get_config_value('API', 'VariancePercent')
            temp_upper_bound = round(api_data * (1 + int(variance_perc) / 100), 2)
            temp_lower_bound = round(api_data * (1 - int(variance_perc) / 100), 2)
            print(f"Temperature upper bound :  {temp_upper_bound} and the temperature Lower bound : {temp_lower_bound}")
            self.assertTrue(temp_upper_bound > ndtv_data > temp_lower_bound,
                            "Temperature reported by NDTV is not as reported by API.")
        else:
            print("Could fetch NDTV weather data or API weather data..!!")
