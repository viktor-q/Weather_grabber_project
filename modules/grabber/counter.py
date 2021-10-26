from modules.grabber.grabber_gecko import grabber_ge
parcer = grabber_ge()

#ya_url = 'https://yandex.ru/pogoda/saint-petersburg'
#gis_url = 'http://www.gismeteo.ru/weather-sankt-peterburg-4079/'
#gidromet_url = 'http://old.meteoinfo.ru/forecasts5000/russia/leningrad-region/sankt-peterburg'
class counter:
    def __init__(self):
        self.grerbgtf = 1
# Считаем среднее арифметическое
    def count(self, ya_url, gis_url, gidromet_url):
        yaweather_for_int = 0
        if (parcer.yandex_weather(ya_url)[0]) == "−":
            yaweather_for_int = (0 - float(parcer.yandex_weather(ya_url)[1:]))
        else:
            yaweather_for_int = float(parcer.yandex_weather(ya_url)[1:])
#print(yaweather_for_int)

        gisweather_for_int = 0
        if (parcer.gismeteo_weather(gis_url)[0]) == "−":
            gisweather_for_int = (0 - float(parcer.gismeteo_weather(gis_url)[1:]))
        else:
            gisweather_for_int = float(parcer.gismeteo_weather(gis_url)[1:])
#print(gisweather_for_int)

        gidrometweather_for_int = float(parcer.gidromet_weather(gidromet_url))
        if (parcer.gidromet_weather(gidromet_url)[0]) == "-":
            gidrometweather_for_int = (0 - float(parcer.gidromet_weather(gidromet_url)[1:]))
        else:
            gidrometweather_for_int = float(parcer.gidromet_weather(gidromet_url)[0:])
#print(gidrometweather_for_int)


        rounds = round((yaweather_for_int + gisweather_for_int + gidrometweather_for_int)/3, 1)

        print('А в среднем сейчас', rounds)
        return rounds