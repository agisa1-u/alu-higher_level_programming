# python-network_1

HTTP requests in Python with `urllib` and `requests`.

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `urllib` and displays the body |
| `1-hbtn_header.py` | Displays the `X-Request-Id` header value of a URL's response (`urllib`) |
| `2-post_email.py` | POSTs an `email` to a URL and displays the response body (`urllib`) |
| `3-error_code.py` | Displays the body of a response, or `Error code: <status>` on an `HTTPError` (`urllib`) |
| `4-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `requests` |
| `5-hbtn_header.py` | Displays the `X-Request-Id` header value of a URL's response (`requests`) |
| `6-post_email.py` | POSTs an `email` to a URL and displays the response body (`requests`) |
| `7-error_code.py` | Displays the body of a response, or `Error code: <status>` if the status is >= 400 (`requests`) |
| `8-json_api.py` | POSTs a letter as `q` to `http://0.0.0.0:5000/search_user` and displays `[<id>] <name>` |
| `10-my_github.py` | Displays your GitHub id using Basic Authentication with a personal access token |
