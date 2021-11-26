import requests
r = requests.get("https://news.ycombinator.com/newest")
if not r.ok:
    print("Запрос не удался. Код ошибки:", r.status_code)
else:
    pass 

