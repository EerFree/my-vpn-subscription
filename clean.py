import os

input_file = "original.txt"
output_file = "cleaned_subscription.txt"

if not os.path.exists(input_file):
    print(f"Ошибка: Файл {input_file} не был скачан сервером!")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Делим текст на строки
lines = text.splitlines()

# Фильтруем: убираем пустые строки и строки, начинающиеся со знака #
cleaned_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]

# Записываем результат
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

print(f"Успешно обработано! Сохранено строк: {len(cleaned_lines)}")
