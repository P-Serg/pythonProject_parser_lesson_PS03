import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # print(response.text)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "word": english_word,
            "w_definition": word_definition
        }
    except:
        print("Произошла ошибка")
def word_dict_translator():
  translator = Translator()
  word_dict = get_english_word()
  word = word_dict.get("word")
  word_definition = word_dict.get("w_definition")
  ru_word = translator.translate(word, dest="ru").text
  ru_definition = translator.translate(word_definition, dest="ru").text
  return {
    "r_word": ru_word,
    "r_w_definition": ru_definition
  }

def word_game():
    print("Добро пожаловать в игру 'Слова'")

    while True:
        word_dict = word_dict_translator()
        word = word_dict.get("r_word")
        r_definition = word_dict.get("r_w_definition")

        print(f"Значение слова - {r_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Правильно!")
        else:
            print(f"Неправильно. Правильное значение - {word}")

        play_again = input("Хотите сыграть еще? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()

