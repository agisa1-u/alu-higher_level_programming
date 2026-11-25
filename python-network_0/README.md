# python-network_0

Bash scripts that use `curl` to talk to a web server.

| File | Description |
| --- | --- |
| `0-body_size.sh` | Displays the size (in bytes) of the body of the response to a URL |
| `1-body.sh` | Sends a GET request and displays the body only for a 200 status code |
| `2-delete.sh` | Sends a DELETE request and displays the body of the response |
| `3-methods.sh` | Displays all the HTTP methods the server accepts (from the `Allow` header of an OPTIONS request) |
| `4-header.sh` | Sends a GET request with the header `X-HolbertonSchool-User-Id: 98` and displays the body |
| `5-post_params.sh` | Sends a POST request with `email` and `subject` and displays the body |
