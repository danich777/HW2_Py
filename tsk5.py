# Написать программу, которая будет выводить в консоль заданный текст
# (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и удалять в заданном тексте
# все слова в которых присутствует введенный шаблон
#
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире


my_text = 'Python - один из самых популярных языков программирования в мире'
print(my_text)

my_text = my_text.split()

sub_str = input('Введите подстроку: ')

new_text = []

for word in my_text:
    if sub_str not in my_text:
        new_text.append(word)

print(' '.join(new_text))
