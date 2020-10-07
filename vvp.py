import json

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from pygal_maps_world.maps import World

from country_code import get_country_code

# Список заполняется данными.
filename = 'vvp.json'
with open(filename) as f:
    vvp_data = json.load(f)

# Построение словаря с данными ВВП по странам за 2016 год.
cc_vvp = {}
for vvp_dict in vvp_data:
    if vvp_dict['Year'] == 2016:
        country_name = vvp_dict['Country Name']
        vvp = int(float(vvp_dict['Value']))/1000
        code = get_country_code(country_name)
        if code:
            cc_vvp[code] = vvp
            print(code + ": " + country_name + " " + str(vvp))
        else:
            print('ERROR - ' + country_name)

# Группировка стран по 3 уровням населения.
cc_vvp_1, cc_vvp_2, cc_vvp_3 = {}, {}, {}
for cc, vvp in cc_vvp.items():
    if vvp < 10000000:
        cc_vvp_1[cc] = vvp
    elif vvp < 100000000:
        cc_vvp_2[cc] = vvp
    else:
        cc_vvp_3[cc] = vvp

# Проверка количества стран на каждом уровне.
print(len(cc_vvp_1), len(cc_vvp_2), len(cc_vvp_3))


wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'ВВП по странам в 2016 году.'
wm.add('< 10 млрд', cc_vvp_1)
wm.add('10 - 100 млрд', cc_vvp_2)
wm.add('> 100 млрд', cc_vvp_3)

wm.render_to_file('world_vvp.svg')