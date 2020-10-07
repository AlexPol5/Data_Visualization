from pygal_maps_world.maps import World

wm = World()
wm.title = 'Население стран Северной Америки'
wm.add('Северная Америка', {'ca': 34126000, 'us': 309349000, 'mx':
                            113423000})

wm.render_to_file('na_populations.svg')