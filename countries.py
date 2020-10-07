#from pygal_maps_world import i18n
#from i18n import COUNTRIES

from pygal_maps_world.maps import COUNTRIES

# Получение и выведение кодов стран в алфавитном порядке.
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])