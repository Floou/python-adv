# 1
from datetime import datetime

date = lambda d: datetime.strptime(d, '%d.%m.%Y').date()


assert date('01.01.2021')
assert date('10.01.2021')
assert date('31.01.2021')

# 2
import re

RE_NUMBER_VALIDATOR = re.compile(r'^(\d{1}[./,]){1}\d{2}$')


def number_is_valid(number):
    return RE_NUMBER_VALIDATOR.match(number)


assert number_is_valid('1.32')
assert number_is_valid('1,32')
