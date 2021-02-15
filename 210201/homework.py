import os
import urllib.parse
import urllib.request
import re
import requests

RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')
RE_PNG_FILE = re.compile(r'href="([^"А-Яа-яЁё]+\.png)"')
request_url = 'https://kpk.kss45.ru/учебная-работа/расписание_пар.html'

response = requests.get(request_url)
content = response.content.decode(encoding=response.encoding)

parsed = RE_XLS_FILE.findall(content)

pass


def url_encode(request_url):
    protocol, address = request_url.split(':', maxsplit=1)
    return ':'.join([protocol, urllib.parse.quote(address)])


with open('Расписание.txt', 'w', encoding='utf-8') as f:
    path = "xml/"
    if not os.path.isdir(path):
        os.mkdir(path)
    for request_url in parsed:
        urllib.request.urlretrieve(
            url_encode(request_url),
            os.path.join(path, request_url.split('/')[-1])
        )