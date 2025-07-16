import time

try:
    from ddgs.exceptions import *
    from ddgs import DDGS
except ModuleNotFoundError:
    raise Exception("[!] Зависимости не найдены, вы можете установить их командой pip/pip3 install -r requirements.txt")


def search(fio, keywords=[]):
    found = ''
    ks = " ".join(f"\"{keyword}\"" for keyword in keywords)

    query = (f"\"{fio}\" " + ks)

    files_queries = [
        "filetype:pdf " + f"\"{fio}\"" + ks,
        "filetype:doc " + f"\"{fio}\"" + ks,
        "filetype:docx " + f"\"{fio}\"" + ks,
        "filetype:ppt " + f"\"{fio}\"" + ks,
        "filetype:pptx " + f"\"{fio}\"" + ks,
        "filetype:csv " + f"\"{fio}\"" + ks,
        "filetype:xls " + f"\"{fio}\"" + ks,
        "filetype:xlsx " + f"\"{fio}\"" + ks,
        "filetype:txt " + f"\"{fio}\"" + ks
    ]

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            if results:
                print("\n[+] Результаты поиска в DuckDuckGo")
                found += "\n\n[+] Результаты поиска в DuckDuckGo"
                for r in results:
                    print(f"\n{r['href']} | {r['title']}")
                    found += f"\n\n{r['href']} | {r['title']}"
            else:
                print("\n[X] Нету результатов поиска в DuckDuckGo")
                found += "\n\n[X] Нету результатов поиска в DuckDuckGo"

            print("\n[+] Результаты поиска по файлам в DuckDuckGo")
            found += "\n\n[+] Результаты поиска по файлам в DuckDuckGo"

            time.sleep(0.5)
            for files_query in files_queries:
                time.sleep(0.5)
                file_results = ddgs.text(files_query)
                if file_results:
                    for r in file_results:
                        if 'http://www.google.com/search?' in r["href"]:
                            continue
                        print(f"\n{r['href']} | {r['title']}")
                        found += f"\n\n{r['href']} | {r['title']}"

    except DuckDuckGoSearchException:
        print("\n[!] Слишком много запросов в DuckDuckGo, попробуйте сменить айпи")
        found += "\n\n[!] Слишком много запросов в DuckDuckGo, попробуйте сменить айпи"

    return found
