d = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",  
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",  
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",  
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",  
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",  
     "б": "b", "ю": "ju", "ё": "jo"}
f = open('cyrillic.txt')
g = open('transliteration.txt', 'w')
for i in f:
    for j in i:
        if j.lower() in d:
            if j.isupper():
                g.write(d[j.lower()].capitalize())
            else:
                g.write(d[j])
        else: 
            g.write(j)
f.close()
g.close()