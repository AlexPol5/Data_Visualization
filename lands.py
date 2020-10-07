import csv

from matplotlib import pyplot as plt

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from pygal_maps_world.maps import World

from country_code import get_country_code

# Чтение площади земли по странам из файла.
filename = 'API_lands.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Построение словаря с данными площади земли по странам за 2018 год.
    cc_lands = {}
    lands = []
    for row in reader:
        try:
        # country =
            country_name = row[0]
            land = int(float(row[62]))
            code = get_country_code(country_name)
            if code:
                cc_lands[code] = land
                print(code + ": " + country_name + " " + str(land))
            else:
                print('ERROR - ' + country_name)
        except ValueError:
            print(land, 'missing data')
        else:
            lands.append(land)

# Группировка стран по 3 уровням площади земли.
cc_land_1, cc_land_2, cc_land_3 = {}, {}, {}
for cc, land in cc_lands.items():
    if land < 100000:
        cc_land_1[cc] = land
    elif land < 1000000:
        cc_land_2[cc] = land
    else:
        cc_land_3[cc] = land

# Проверка количества стран на каждом уровне.
print(len(cc_land_1), len(cc_land_2), len(cc_land_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Площадь земли по странам в 2018 году.'
wm.add('< 100 тыс.кв.км.', cc_land_1)
wm.add('100 тыс. - 1 млн.кв.км.', cc_land_2)
wm.add('> 1 млн.кв.км.', cc_land_3)

wm.render_to_file('world_lands.svg')