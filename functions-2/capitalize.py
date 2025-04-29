def capitalize(word):
    # Перетворюємо першу літеру на велику, якщо слово не порожнє
    if len(word) > 0:
        return chr(ord(word[0]) - 32) + word[1:]
    return word

def capitalize_sentence(sentence):
    # Розбиваємо речення на слова, застосовуємо capitalize() до кожного слова
    words = sentence.split(' ')
    capitalized_words = [capitalize(word) for word in words]
    # Об'єднуємо слова назад у речення
    return ' '.join(capitalized_words)

# Приклад використання
input_sentence = input("Введіть рядок: ")
print(capitalize_sentence(input_sentence))