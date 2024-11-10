# Code-Crushers
Desicion for case "Library searcher"
## Как установить и запустить
### Требования
Для установки и запуска, нужен [Python 3+](https://python.org), [Git](https://git-scm.com/), [Node JS](https://nodejs.org/en),[Flask](https://flask.palletsprojects.com/en/stable/)
### Процесс установки и запуска
1. Клонировать репозиторий
```
git clone https://github.com/SanyaLikeIT/Code-Crushers.git
```
2. Установить все нужные библиотеки
```
pip install -r requirements.txt
```
3. Выполнить команды
```
node server.js
python app.py
```
4. Перейти по адресу из консоли и начать пользоваться сервисом
## Как устроена модель поиска
Вся программа разделена на 4 файла: 
### main.py
Точка входа программы. В файле реализовано общение модели и пользователя.
### vectorstor.py
Реализовано 2 функции: load_pdf_from_foalder для считывания всех данных pdf файлов в txt формате document (формат langchain), vectorsto для эмбединга полученного из pdf текста.
### retrieve.py
Реализация RAG
### config.py
Реализация работы с yandexGPT и задание system промпта.
Требудется указать свой токен для работы с yandexGPT.
Настроить yandexGPT API можно по [ссылке](https://yandex.cloud/ru/docs/foundation-models/quickstart/yandexgpt?utm_referrer=https%3A%2F%2Fwww.google.com%2F)
