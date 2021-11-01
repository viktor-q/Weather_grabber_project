import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class grabber_ge:
    def __init__(self):
        self.grerbgtf = 1

    def yandex_weather(self, ya_url):
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=r"/usr/local/bin/geckodriver")
        driver.set_window_size(1440, 900)
        driver.get(ya_url)

        tag_list = driver.find_elements_by_class_name("fact__temp-wrap")

        weather_alltext = []
        for e in tag_list:
            weather_alltext.append(e.text)
        str_weather_alltext = weather_alltext[0].split(sep="\n")

        driver.quit()

        return str_weather_alltext[0]

    def gismeteo_weather(self, gis_url):
        response = requests.get(gis_url, headers={"User-Agent": UserAgent().chrome})
        soup = BeautifulSoup(response.text, "lxml")
        weather_all = soup.find_all("span", class_="js_value tab-weather__value_l")

        weather_alltext = []

        for weather_now in weather_all:
            weather_alltext.append(weather_now.text.replace("\n", "").replace(" ", ""))

        return weather_alltext[0].replace(",", ".")

    def gidromet_weather(self, gidromet_url):
        response = requests.get(gidromet_url)
        soup = BeautifulSoup(response.text, "lxml")
        weather_all = soup.find_all(class_="pogodacell")

        weather_alltext = []

        for weather_now in weather_all:
            weather_alltext.append(weather_now.text)

        #    return (weather_alltext[7])[7:]
        return (weather_alltext[7])[6:]


# test = grabber_ge()
# from modules.databases import city_links_base
# xxx = city_links_base.regions[78]['yandex']
# print(xxx)
# print('Яндекс говорит что сейчас', test.yandex_weather(xxx))
