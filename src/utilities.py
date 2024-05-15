import sys
import json
import logging
import os
import requests
from bs4 import BeautifulSoup
import http.client, urllib

user_key = os.environ.get("user_key")
api_token = os.environ.get("api_token")

loglevel = os.environ.get("LOGGING_LEVEL", logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(loglevel)
# logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def log_line(event, status, **record):
    logger.info(
        json.dumps(
            {
                "event": event,
                "status": status,
                **record,
            },
            default=str,
        )
    )


def get_html(url):
    log_line("get_html", "start", url=url)
    r = requests.get(url)
    log_line("get_html", "end", status_code=r.status_code)
    return r.text


def in_stock(html):
    log_line("in_stock", "start")
    soup = BeautifulSoup(html, "html.parser")
    button = soup.find(
        "button",
        class_="product-form__submit button button--full-width button--secondary",
    )
    if button:
        span = button.find("span")
        inner_text = span.get_text()
    if "Sold" in inner_text:
        log_line("in_stock", "end", in_stock=False)
        return False
    else:
        log_line("in_stock", "end", in_stock=True)
        return True


def send_push_notification(message):
    log_line("send_push_notification", "start", message=message)
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
    log_line("send_push_notification", "end", message=message)
