from duckduckgo_search import DDGS

def search(fio):
    found = ''

    query = f"\"{fio}\""
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

    return found