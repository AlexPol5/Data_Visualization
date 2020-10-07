import json

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from pygal_maps_world.maps import World

from country_code import get_country_code

# Список заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Построение словаря с данными численности населения за 2010 год.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            print(code + ": "+ country_name)
        else:
            print('ERROR - ' + country_name)

# Группировка стран по 3 уровням населения.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Проверка количества стран на каждом уровне.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Население мира в 2010 году, по странам.'
wm.add('0-10 млн', cc_pops_1)
wm.add('10 млн - 1 млрд', cc_pops_2)
wm.add('> 1 млрд', cc_pops_3)

wm.render_to_file('world_populations.svg')