import sys

sys.path.append(".")

from utilities import log_line, get_html, in_stock, send_push_notification


sold_out_html = "<html><body><button class='product-form__submit button button--full-width button--secondary'><span>Sold Out</span></button></body></html>"
in_stock_html = "<html><body><button class='product-form__submit button button--full-width button--secondary'><span>Buy Now</span></button></body></html>"


def test_get_html():
    url = "https://www.google.com"
    html = get_html(url)
    assert html is not None


def test_in_stock():
    assert in_stock(in_stock_html) == True


def test_not_in_stock():
    assert in_stock(sold_out_html) == False
