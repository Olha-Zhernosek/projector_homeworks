import requests

'''Create a program that allows you to search for images
in gif format. The program should allow you to enter a
search word. Using this word, search for GIFs using the
Giphy API. As a result, print the links to the GIFs. '''


def get_api_key():
    try:
        with open("api_key.txt", "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        print("Файл api_key.txt не знайдено.")
        return None


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
