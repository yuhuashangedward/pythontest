import requests

bad_r = requests.get('http://httpbin.org/status/404')

print(bad_r.status_code)

bad_r.raise_for_status()