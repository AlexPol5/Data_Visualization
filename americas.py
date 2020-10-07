from pygal_maps_world.maps import World

wm = World()
wm.title = 'Северная, Центральная и Южная Америка'

wm.add('Северная Америка', ['ca', 'mx', 'us'])
wm.add('Центральная Америка', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Южная Америка', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')