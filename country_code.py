from pygal_maps_world.maps import COUNTRIES

def get_country_code(country_name):
    """Возвращает для заданной страны её код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

        if country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Tanzania':
            return 'tz'

    # Если страна не найдена, вернуть None.
    return None


