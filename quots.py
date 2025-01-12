file = open('quotes.txt', 'r', encoding='utf-8')
verse = file.read()
file.close()
print(verse)

author = input("Хто автор?")

with open('quotes.txt', 'a', encoding='utf-8') as file:
    file.write('(' + author + ')\n')

while True:
    answer = input("Хочете ввести ще одну цитату?(так/ні)")
    answer = answer.lower()
    if answer == 'так':
        quot = input("Введіть цитату")
        author = input("Введіть автора")
        file = open("quotes.txt", "a", encoding="utf-8")
        file.write(quot + ": " + author + '\n')
        file.close()
    else:
        break