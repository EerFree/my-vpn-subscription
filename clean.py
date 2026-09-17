name: Auto Clean VPN List

on:
  schedule:
    - cron: '0 * * * *'  # Запуск каждый час
  workflow_dispatch:     # Кнопка для ручного запуска

jobs:
  run-cleaner:
    runs-on: ubuntu-latest

    steps:
    - name: Клонирование репозитория
      uses: actions/checkout@v4

    - name: Настраиваем Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Скачивание оригинального файла через curl
      run: |
        curl -sL "https://githubusercontent.com" -o original.txt

    - name: Выполнение скрипта очистки
      run: python clean.py

    - name: Запись очищенного файла обратно в репозиторий
      run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@://github.com"
        git add cleaned_subscription.txt
        git commit -m "Автоматическое обновление подписки (удалены комментарии)" || exit 0
        git push
