import time

try:
    from ddgs.exceptions import *
    from ddgs import DDGS
except ModuleNotFoundError:
    raise Exception("[!] Зависимости не найдены, вы можете установить их командой pip/pip3 install -r requirements.txt")


def search(fio, keywords=[]):
    found = ''
    ks = " + ".join(f"\"{keyword}\"" for keyword in keywords)

    query = (f"\"{fio}\" " + ks)

    files_queries = [
        "filetype:pdf " + query,
        "filetype:doc " + query,
        "filetype:docx " + query,
        "filetype:ppt " + query,
        "filetype:pptx " + query,
        "filetype:csv " + query,
        "filetype:xls " + query,
        "filetype:xlsx " + query,
        "filetype:txt " + query
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

            for files_query in files_queries:
                time.sleep(0.5)
                file_results = ddgs.text(files_query)
                if file_results:
                    for r in file_results:
                        if 'http://www.google.com/search?' in r["href"]:
                            continue
                        print(f"\n{r['href']} | {r['title']}")
                        found += f"\n\n{r['href']} | {r['title']}"

    except Exception as e:
        print(f"\n[!] Произошла ошибка: {e}")

    return found
