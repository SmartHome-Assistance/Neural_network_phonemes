from os import path
filename = 'comm_dict.dic'
if (path.isfile(filename)):
    f = open(filename, 'a')
else:
    f = open(filename, 'w')

phonemes = {'М': 'm', 'а': 'a', 'к': 'k', 'с': 's', 'в': 'v', 'л': 'l', 'ю': 'ju', 'ч': 'ch', 'и': 'i', 'е': 'e', 'т': 't', 'ы': 'i'}

words = ["Макс", "включи", "выключи", "свет"]

for word in words:
    f.write(word + ' ')
    for letter in word:
        f.write(phonemes[letter] + ' ')
    f.write('\n')
f.close()
