from flask import Flask, render_template
import requests
import time


# Get Random Quote Function
def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Failed to retrieve a quote."


quote_gen_site = Flask(__name__)
quote = get_random_quote()


# Home Page Route
@quote_gen_site.route("/")
def home_page():
    return render_template('index.html', quote=quote)


if __name__ == "__main__":
    quote_gen_site.run(debug=True)
    time.sleep(1)
