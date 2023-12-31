import requests
import os

'''Create a program that allows you to search for images
in gif format. The program should allow you to enter a
search word. Using this word, search for GIFs using the
Giphy API. As a result, print the links to the GIFs. '''


def get_api_key():
    api_key_file = 'api_key.txt'

    if os.path.isfile(api_key_file):
        with open(api_key_file, 'r') as file:
            return file.readline().strip()
    else:
        raise Exception("Файл api_key.txt не знайдено. Будь ласка, додайте ваш API ключ у цей файл.")


def search_gifs(query):
    api_key = get_api_key()

    if api_key is None:
        return []

    base_url = "http://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": 5
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        gif_links = [gif["images"]["original"]["url"] for gif in data["data"]]
        return gif_links
    else:
        print("Помилка отримання GIF-зображень:", data.get("message", "Невідома помилка"))
        return []


def main():
    search_query = input("Введіть слово для пошуку: ")
    gif_links = search_gifs(search_query)

    if gif_links:
        print("Знайдені GIF-зображення:")
        for link in gif_links:
            print(link)
    else:
        print("GIF-зображення не знайдено.")


if __name__ == "__main__":
    main()
