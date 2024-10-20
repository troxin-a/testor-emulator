# Тестовое задание

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-lightgreen)
![SQLalchemy](https://img.shields.io/badge/SQLalchemy-2.0-red)
![alembic](https://img.shields.io/badge/Alembic-1.13-red)
![pyjwt](https://img.shields.io/badge/Pyjwt-2.9-yellow)
![SQLAdmin](https://img.shields.io/badge/SQLAdmin-0.2-black)


## 🛠️ Установка

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/troxin-a/testor-emulator.git
cd testor-emulator
```

2. **Создайте файл .env в корневом каталоге проекта и добавьте необходимые переменные окружения:**

```bash
cp .env.sample .env
nano .env
```

3. **Запустите docker-compose файл с билдом:**

```bash
docker compose up -d --build
```

4. **Примените миграции:**

```bash
docker compose exec app1 alembic upgrade head
```


## 📚️ Использование
Админ-панель доступна по адресу: http://127.0.0.1:8000/admin/<br>
Только пользователь admin@admin.ru может туда попасть (необходимо создать этого пользователя). Да, это хардкод! :)<br>
Документация по использованию API будет доступна после запуска сервера по ссылке: http://127.0.0.1:8000/docs/