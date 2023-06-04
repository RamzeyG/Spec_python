## -*- coding: utf-8 -*-

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import re 

with open("D:/GB/spec/python/Seminar_3/1.txt", encoding='utf-8') as file:
    a = file.read()
    
    new = a.replace('[', '').replace(']', '').replace(',', '').replace('.', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '').replace('\n\n', ' ').replace(')', '').replace('(', '').replace('-', '').replace('—', '').replace('»', '')

    b = new.lower().split(' ')

    letters = b
    frequency = {}

    for letter in letters:
        frequency[letter] = frequency.get(letter, 0) + 1

    list_f = list(frequency.items())

    list_f.sort(key=lambda i: i[1], reverse = True)


    print(f"В тексте {len(letters)} слов")

    for i in range(10):
        print(f"Слово '{list_f[i][0]}' встречается {list_f[i][1]} раз")