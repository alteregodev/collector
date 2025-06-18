from duckduckgo_search.exceptions import *
from duckduckgo_search import DDGS

def search(fio, keywords=[]):
    found = ''

    query = (f"\"{fio}\" " + " ".join(f"\"{keyword}\"" for keyword in keywords))
    files_query = (f"filetype:pdf | filetype:doc | filetype:docx | filetype:ppt | filetype:pptx | filetype:csv | filetype:xls | filetype:xlsx \"{fio}\" " + " ".join(f"\"{keyword}\"" for keyword in keywords))

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            if results:
                print("\n[+] Результаты поиска в DuckDuckGo")
                found += "\n\n[+] Результаты поиска в DuckDuckGo"
                for r in results:
                    print(f"\n{r["href"]} | {r["title"]}")
                    found += f"\n\n{r["href"]} | {r["title"]}"
            else:
                print("\n[X] Нету результатов поиска в DuckDuckGo")
                found += "\n\n[X] Нету результатов поиска в DuckDuckGo"

            file_results = ddgs.text(files_query)
            if file_results:
                print("\n[+] Результаты поиска по файлам в DuckDuckGo")
                found += "\n\n[+] Результаты поиска по файлам в DuckDuckGo"
                for r in results:
                    print(f"\n{r["href"]} | {r["title"]}")
                    found += f"\n\n{r["href"]} | {r["title"]}"
            else:
                print("\n[X] Нету результатов поиска по файлам в DuckDuckGo")
                found += "\n\n[X] Нету результатов поиска по файлам в DuckDuckGo"

    except DuckDuckGoSearchException:
        print("\n[!] Слишком много запросов в DuckDuckGo, попробуйте сменить VPN")
        found += "\n\n[!] Слишком много запросов в DuckDuckGo, попробуйте сменить VPN"

    return found