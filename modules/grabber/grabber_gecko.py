# weather_grab
# 26.10.2021
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ya_url = 'https://yandex.ru/pogoda/saint-petersburg'
#ya_url = 'https://yandex.ru/pogoda/krasnodar'

gis_url = 'http://www.gismeteo.ru/weather-sankt-peterburg-4079/'
#gis_url = 'https://www.gismeteo.ru/weather-kaluga-4387/'

gidromet_url = 'http://old.meteoinfo.ru/forecasts5000/russia/leningrad-region/sankt-peterburg'

class grabber_ge:
    def __init__(self):
        self.grerbgtf = 1


    def yandex_weather(self, ya_url):
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=r'/usr/local/bin/geckodriver')
        driver.set_window_size(1440, 900)
        driver.get(ya_url)

        tag_list = driver.find_elements_by_class_name('fact__temp-wrap')

        weather_alltext = []
        for e in tag_list:
            weather_alltext.append(e.text)
        str_weather_alltext = weather_alltext[0].split(sep='\n')

        driver.quit()

        return(str_weather_alltext[0])




    def gismeteo_weather(self, gis_url):
        response = requests.get(gis_url, headers={'User-Agent': UserAgent().chrome})
        soup = BeautifulSoup(response.text, 'lxml')
        weather_all = soup.find_all('span', class_="js_value tab-weather__value_l")

        weather_alltext = []

        for weather_now in weather_all:
            weather_alltext.append(weather_now.text.replace('\n','').replace(' ',''))

        return weather_alltext[0].replace(',','.')

    def gidromet_weather(self, gidromet_url):
        response = requests.get(gidromet_url)
        soup = BeautifulSoup(response.text, 'lxml')
        weather_all = soup.find_all(class_="pogodacell")

        weather_alltext = []

        for weather_now in weather_all:
            weather_alltext.append(weather_now.text)

#    return (weather_alltext[7])[7:]
        return (weather_alltext[7])[6:]

#    print('Яндекс говорит что сейчас', yandex_weather(ya_url))
#    print('Гисметео говорит что сейчас', gismeteo_weather(gis_url))
#    print('Гидрометцентр говорит что сейчас', gidromet_weather(gidromet_url))


# Считаем среднее арифметическое
#    yaweather_for_int = 0
#    if (yandex_weather(ya_url)[0]) == "−":
#        yaweather_for_int = (0 - float(yandex_weather(ya_url)[1:]))
#    else:
#        yaweather_for_int = float(yandex_weather(ya_url)[1:])
#print(yaweather_for_int)

#    gisweather_for_int = 0
#    if (gismeteo_weather(gis_url)[0]) == "−":
#        gisweather_for_int = (0 - float(gismeteo_weather(gis_url)[1:]))
#    else:
#        gisweather_for_int = float(gismeteo_weather(gis_url)[1:])
#print(gisweather_for_int)

#    gidrometweather_for_int = float(gidromet_weather(gidromet_url))
#if (gidromet_weather(gidromet_url)[0]) == "-":
#    gidrometweather_for_int = (0 - float(gidromet_weather(gidromet_url)[1:]))
#else:
#    gidrometweather_for_int = float(gidromet_weather(gidromet_url)[1:])
#print(gidrometweather_for_int)


#    rounds = round((yaweather_for_int + gisweather_for_int + gidrometweather_for_int)/3, 1)
#    print('А в среднем сейчас', rounds)

