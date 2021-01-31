import re

RE_DATA_VALIDATOR = re.compile(r'^[0-9]{2,}.+[0-9]{2},+[0-9]{4}$')

def data_is_valid(data):
    return RE_DATA_VALIDATOR.match(data)


assert data_is_valid('25.01.2021')

