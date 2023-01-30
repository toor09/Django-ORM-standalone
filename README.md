# Пульт охраны для банка

## Установка

- Скачайте код.
- Установите актуальную версию poetry в `UNIX`-подобных дистрибутивах с помощью команды:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```
или в `Windows Powershell`:
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
- Добавьте к переменной окружения `$PATH` команду poetry:
```
source $HOME/.poetry/bin
```
- Установите виртуальное окружение в директории с проектом командой:
```
poetry config virtualenvs.in-project true
```
- Установите все зависимости (для установки без dev зависимостей можно добавить аргумент `--no-dev`):
```
poetry install
```
- Активируйте виртуальное окружение командой: 
```
source .venv/bin/activate
```

## Настройка переменных окружения

- Cоздайте файл `.env` в директории проекта, на основе файла `.env.example` командой 
(при необходимости скорректируйте значения переменных окружения):
```
cp .env.example .env
```
<details>
  <summary>Переменные окружения</summary>
  <pre>
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    SECRET_KEY=
    DEBUG=False
    ALLOWED_HOSTS=
  </pre>
</details>

Для генерации значения переменной окружения `SECRET_KEY` можно воспользоваться функцией встроенного модуля `secrets`:

```python3
import secrets
secret_token = secrets.token_urlsafe(nbytes=64)
```

*** Группа переменных окружения, которая начинается с `DB_`, предназначена для подключения к базе данных для пульта охраны. ***

*** Для переключения в режим дебага нужно установить значение переменной окружения `DEBUG=True` (!!! использовать только для локальной отладки !!!) ***

*** В случае, когда `DEBUG=False`, необходимо заполнить переменную окружения `ALLOWED_HOSTS`. ***

## Запуск линтеров

```
isort . && flake8 . && mypy .
```

## Запуск

- Для запуска пульта охраны для банка вводим команду:
```
python3 manage.py runserver
```

## Цели проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).
