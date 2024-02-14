# Django Store



[![Join our Discord](https://img.shields.io/badge/Discord-IT-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/tuuy5VqGgw)



Django Store - это онлайн магазин для покупок не только вещей для повседневной носки, но и для покупок подароков любимым людям.
![Django store Products](/img.png "Продукты")
- ✨Magic ✨

## Stack

- Python 3.10+
- Django 3.2.12


## Installation

##### Вызов команд для **Linux/Mac**:

**`./manage.py`**

##### Команды для **Windows**:

**`python manage.py`**

#### Установка проекта:
1. Создание миграции<br />
`./manage.py makemigrations`
2. Подключение миграции<br />
`./manage.py migrate`
3. Создание суперпользователя<br />
`./manage.py createsuperuser`
4. Подгрузка Фикстур<br />
`./manage.py loaddata products/fixtures/categoris.json`<br />
`./manage.py loaddata products/fixtures/goods.json`

#### Полезные команды для разработки:
1. Сохранение базы данных (категории):<br />
    Linux:  <br />`./manage.py dumpdata products.ProductCategory > categories.json`<br />
    Windows: <br />`python  -Xutf8 manage.py dumpdata products.ProductCategory -o categories.json`<br />
2. Сохранение базы данных (продукты):<br />
    Linux: <br /> `./manage.py dumpdata products.Product > goods.json`<br />
    Windows: <br />`python  -Xutf8 manage.py dumpdata products.Product -o goods.json`<br />



Проверьте развертывание, перейдя по адресу вашего сервера в предпочитаемый вами браузер.

```sh
127.0.0.1:8000
```

