import os
import requests
from bs4 import BeautifulSoup
import http.client, urllib


user_key = os.environ.get("user_key")
api_token = os.environ.get("api_token")


def get_html(url):
    r = requests.get(url)
    return r.text


def in_stock(html):
    soup = BeautifulSoup(html, "html.parser")
    button = soup.find(
        "button",
        class_="product-form__submit button button--full-width button--secondary",
    )
    if button:
        span = button.find("span")
        inner_text = span.get_text()
    if "Sold" in inner_text:
        return False
    else:
        return True


def send_push_notification(user_key, api_token, message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": f"{api_token}",
                "user": f"{user_key}",
                "message": f"Dirtywave M8 is: {message}",
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()


def lambda_handler(event, context):
    url = "https://dirtywave.com/products/m8-tracker-model-02"
    html = get_html(url)

    if in_stock(html):
        print("In stock")
        send_push_notification(user_key, api_token, "In stock")



lambda_handler(None, None)