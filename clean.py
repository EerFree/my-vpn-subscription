import requests

url = "https://githubusercontent.com"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    
    # Фильтруем строки от комментариев и пустых строк
    lines = response.text.splitlines()
    cleaned_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    
    # Записываем в финальный файл
    with open("cleaned_subscription.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(cleaned_lines))
        
    print("Файл успешно очищен!")
except Exception as e:
    print(f"Ошибка: {e}")
    exit(1)
