from utilities import log_line, get_html, in_stock, send_push_notification


def lambda_handler(event, context):
    try:
        url = "https://dirtywave.com/products/m8-tracker-model-02"
        html = get_html(url)

        if in_stock(html):
            send_push_notification("In stock")
        else:
            send_push_notification("Out of stock")
    except Exception as e:
        log_line("lambda_handler", "error", error=str(e))


lambda_handler(None, None)
