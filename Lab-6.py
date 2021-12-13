import requests
from bs4 import BeautifulSoup

r = requests.get("https://1plus1.ua/tanci-z-zirkami/novyny/tvoa-mria-tvij-den-u-finali-tanci-z-zirkami-italijska-cervona-masina-zavitsa-na-golovnomu-tancuvalnomu-parketi-kraini")

if not r.ok:
    print("Не удалось выполнить запрос. Код ошибки:", r.status_code)
else:
    page = BeautifulSoup(r.text, 'html.parser')
    p = page.select("body > main > div > section > div > article > div.article__center > div p")
    a = page.select("a")
    img = page.select("img")
    words = {}
    for i in p:
        for j in i.get_text().split(' '):
            if not j in words:
                words[j] = 1
                continue

            words[j] += 1

    print("Частота появления слов:", words)
    print("Параграфы:", len(p))
    print("Ссылки:", len(a))
    print("Изображения:", len(img))

