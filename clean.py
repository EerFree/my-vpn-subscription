import requests

# Точная веб-ссылка на страницу подписки
web_url = "https://github.com/igareck/vpn-configs-for-russia/blob/main/BLACK_SS%2BAll_RUS.txt"

# Автоматически пересобираем её в прямую text/raw ссылку, чтобы скачать чистый текст
raw_url = web_url.replace("github.com", "://githubusercontent.com").replace("/blob/", "/")

try:
    # Загружаем файл
    response = requests.get(raw_url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    
    # Делим на строки
    lines = response.text.splitlines()
    
    # Фильтруем: исключаем пустые строки и те, что начинаются с #
    cleaned_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    
    # Сохраняем очищенные конфигурации в текстовый файл
    with open("cleaned_subscription.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(cleaned_lines))
        
    print(f"Очистка завершена успешно! Сохранено рабочих строк: {len(cleaned_lines)}")

except Exception as e:
    print(f"Ошибка при обработке файла: {e}")
    exit(1)

