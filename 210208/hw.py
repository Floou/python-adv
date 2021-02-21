import random
import re



RE_PROVERKA = re.compile(r'[а-яА-Я]+')
f = open('text', 'r', encoding='utf-8')
text = f.read()

print(text)
bad_chars = [';', ':', '?', '.', ',', '!', '~', '\n', '…', '-']

for i in bad_chars:
    text = text.replace(i, ' ')
text = text.split(" ")

slova = [w for w in filter(RE_PROVERKA.match, text)]
print(slova, sep='\n')

i = 0
while i != 20:
    i += 1
    print(i, random.choice(slova))

f.close()