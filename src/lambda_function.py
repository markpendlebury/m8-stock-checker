from utilities import log_line, get_html, in_stock, send_push_notification


def lambda_handler(event, context):
    log_line("lambda_handler", "DEBUG", lambda_event=event)
    try:
        url = "https://dirtywave.com/products/m8-tracker-model-02"
        html = get_html(url)

        teststring = "TEST_STRING"
        log_line("lambda_handler", "DEBUG", teststring=teststring)
        
        lower_case_test_string = teststring.lower()
        log_line("lambda_handler", "DEBUG", lower_case_test_string=lower_case_test_string)

        if event.get("test").lower() == "true":
            if in_stock(html):
                send_push_notification("In stock")
            else:
                send_push_notification("Out of stock")

        if in_stock(html):
            send_push_notification("In stock")

    except Exception as e:
        log_line("lambda_handler", "error", error=str(e))
