import requests
import random

from bs4 import BeautifulSoup


def find(fio):
    found = ''

    url_fio = fio.replace(' ', '+')
    url = f"https://www.list-org.com/search?type=fio&val={url_fio}"

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.57 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Safari/537.36 Edg/123.0.2420.81",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.2365.66",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Safari/537.36 OPR/108.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36"
    ]


    headers = {
        'User-Agent': random.choice(user_agents)
    }

    try:
        html = requests.get(url, timeout=10, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')

        if "Проверка, что Вы не робот" in html:
            print("\n[!] Блокировка ботов от list-org.com, попробуйте cменить айпи")
            return found

        results_card = soup.find(class_='content')

        count = results_card.find('b').text

        if count != '0' and int(count) < 24100000:
            print(f"\n[+] Найдено {count} ИП по ФИО {fio}")
            found += f"\n[+] Найдено {count} ИП по ФИО {fio}"

            results_list = results_card.find_all('p')
            for result in results_list:
                inn = result.text.strip()
                a = result.find('a')
                if a is None:
                    continue

                details = a.get('href', '')
                text = a.text.strip()

                print(f"(http://list-org.com{details}) | {inn}")
                found += f"\n(http://list-org.com{details}) | {inn}"
        else:
            print(f"\n[X] Не найдено ИП по ФИО {fio}")
            found += f"\n[X] Не найдено ИП по ФИО {fio}"
    except Exception as e:
        if f"{e}".strip() == "'NoneType' object has no attribute 'find'":
            print("\n[!] Блокировка ботов от list-org.com, попробуйте сменить айпи")
            found += f"\n[!] Блокировка ботов от list-org.com, попробуйте сменить айпи"
        else:
            print(f"[!] Ошибка во время получения ИП: {e}")
            found += f"\n[!] Ошибка во время получения ИП: {e}"
        return found
    return found
