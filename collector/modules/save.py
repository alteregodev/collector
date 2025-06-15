def save(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
    except FileNotFoundError:
        print('\n[!] Путь к файлу не существует')