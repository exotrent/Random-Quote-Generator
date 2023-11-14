import requests


def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Failed to retrieve a quote."


if __name__ == "__main__":
    quote = get_random_quote()
    print(quote)
