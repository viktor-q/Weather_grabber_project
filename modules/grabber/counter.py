from modules.grabber.grabber_gecko import grabber_ge

parcer = grabber_ge()

# from modules.databases import city_links_base
# ya_url = city_links_base.regions[78]['yandex']
# gis_url = city_links_base.regions[78]['gismeteo']
# gidromet_url = city_links_base.regions[78]['gidromet']


class counter:
    def __init__(self):
        self.grerbgtf = 1

    # Считаем среднее арифметическое
    def count(self, ya_url, gis_url, gidromet_url):
        yaweather_for_int = 0
        if (parcer.yandex_weather(ya_url)[0]) == "−":
            yaweather_for_int = 0 - float(parcer.yandex_weather(ya_url)[1:])
        else:
            yaweather_for_int = float(parcer.yandex_weather(ya_url)[1:])
        # print(yaweather_for_int)

        gisweather_for_int = 0
        if (parcer.gismeteo_weather(gis_url)[0]) == "−":
            gisweather_for_int = 0 - float(parcer.gismeteo_weather(gis_url)[1:])
        else:
            gisweather_for_int = float(parcer.gismeteo_weather(gis_url)[1:])
        # print(gisweather_for_int)

        gidrometweather_for_int = float(parcer.gidromet_weather(gidromet_url))
        if (parcer.gidromet_weather(gidromet_url)[0]) == "-":
            gidrometweather_for_int = 0 - float(parcer.gidromet_weather(gidromet_url)[1:])
        else:
            gidrometweather_for_int = float(parcer.gidromet_weather(gidromet_url)[0:])
        # print(gidrometweather_for_int)

        rounds = round((yaweather_for_int + gisweather_for_int + gidrometweather_for_int) / 3, 1)

        print("А в среднем сейчас", rounds)
        return rounds


# test = counter()
# x_reg = 40
# test.count(city_links_base.regions[x_reg]['yandex'],
#           city_links_base.regions[x_reg]['gismeteo'],
#           city_links_base.regions[x_reg]['gidromet'])
