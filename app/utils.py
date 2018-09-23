# app/utils.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from . import db
from .models.region import Region
from .models.city import City

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def addFake_data():
    '''Добавляет фековые данные регионов и городов'''
    data = {
        'Краснодарский край': ('Краснодар', 'Кропоткин', 'Славянск'),
        'Ростовская область': ('Ростов', 'Шахты', 'Батайск'),
        'Ставропольский край': ('Ставрополь', 'Пятигорск', 'Кисловодск')
    }

    for region_title in data:
        region = Region(title=region_title)

        for city in data[region_title]:
            city = City(title=city, region=region)
            db.session.add(city)

        db.session.add(region)
    db.session.commit()



def flash_errors(form):
    '''Формирует данные о ошибках в форме'''
    all_errors = [] 
    for field, errors in form.errors.items():
        for error in errors:
            all_errors.append({'field': field, 'error': error})
    return all_errors

