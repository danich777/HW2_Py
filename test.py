# исходная строка
line = 'остались строки и перенос слова перекресток переоборудование'

# делим строку на слова
words = line.split(' ')
# фрагмент, по которому будем удалять слова
fragment = 'пере'
# новый список оставшихся слов
new_words = []
for word in words:
     if fragment not in word:
         new_words.append(word)

print(new_words)
