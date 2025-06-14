import requests
from bs4 import BeautifulSoup

def find(fio):
    url_fio = fio.replace(' ', '+')
    url = f"https://www.list-org.com/search?type=fio&val={url_fio}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
    }

    html = requests.get(url, timeout=10, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    results_card = soup.find(class_='content')

    count = results_card.find('b').text

    if count != '0':
        print(f"[+] Найдено {count} ИП по ФИО {fio}")
    else:
        print(f"[+] Не найдено ИП по ФИО {fio}")

    results_list = results_card.find_all('p')
    for result in results_list:
        inn = result.text.strip()
        a = result.find('a')
        if a is None:
            continue

        details = a.get('href', '')
        text = a.text.strip()

        print(f"\n(http://list-org.com{details}) | {inn}")

