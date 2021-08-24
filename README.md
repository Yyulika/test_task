# test_task
DJANGO

Необходимые шаги для инсталляции(pip install django,pip install pymongo,pip install djongo, pip install djangorestframework)
переходите в папку,где находится manage.py,чтобы сделать миграции и запуск сервера
перед запуском нужно сделать( manage.py makemigrations,затем manage.py migrate)
Команда для запуска(manage.py runserver)
Curl-команды:
Для создания товара : http://127.0.0.1:8000/api/product/create/
в поле для создания прописываете,например 
{"title": "Headphones SVEN ",
        "description": "device for listen to music",
        "parameters": {
            "connection": "wired",
            "power": "-",
            "color": "Black"}
}
Я тестировала url через Postman
на выходе получаете:
{
    "id": 22,
    "title": "Headphones SVEN",
    "description": "device for listen to music",
    "parameters": {
        "connection": "wired",
        "power": "-",
        "color": "Black"
    }
}

Для получения списка товаров: http://127.0.0.1:8000/api/products/
получаете список всех товаров,примерно так:
[
    {
        "id": 8,
        "title": "Smartphone Samsung",
        "description": "mobile telephone",
        "parameters": {
            "operation_system": "Android",
            "quantity_core": 8,
            "color": "Black",
            "price": 30000
        }
    },
    {
        "id": 9,
        "title": "Televisor LG",
        "description": "device with screen",
        "parameters": {
            "diagonal": 24,
            "technologies": "LED",
            "color": "Black",
            "price": 15000
        }
    },
    {
        "id": 10,
        "title": "Televisor LG",
        "description": "device with screen",
        "parameters": {
            "diagonal": 48,
            "technologies": "QLED",
            "color": "White",
            "price": 43000
        }
    },
    {
        "id": 11,
        "title": "Televisor Samsung",
        "description": "device with screen",
        "parameters": {
            "diagonal": 54,
            "technologies": "QLED",
            "color": "Black",
            "price": 35000
        }
    },
    {
        "id": 12,
        "title": "Televisor Samsung",
        "description": "device with screen",
        "parameters": {
            "diagonal": 54,
            "technologies": "LED",
            "color": "Black",
            "price": 20000
        }
    },
    {
        "id": 13,
        "title": "Smartphone Iphone 11",
        "description": "mobile telephone",
        "parameters": {
            "operation_system": "IOS",
            "quantity_core": 6,
            "color": "Black",
            "price": 70000
        }
    },
    {
        "id": 14,
        "title": "Smartphone Iphone 11",
        "description": "mobile telephone",
        "parameters": {
            "operation_system": "IOS",
            "quantity_core": 6,
            "color": "White",
            "price": 64000
        }
    },
    

Для поиска по параметрам : http://127.0.0.1:8000/api/products/?search=(например,http://127.0.0.1:8000/api/products/?search="color": "Black")
[
    {
        "id": 8,
        "title": "Smartphone Samsung",
        "description": "mobile telephone",
        "parameters": {
            "operation_system": "Android",
            "quantity_core": 8,
            "color": "Black",
            "price": 30000
        }
    },
    {
        "id": 9,
        "title": "Televisor LG",
        "description": "device with screen",
        "parameters": {
            "diagonal": 24,
            "technologies": "LED",
            "color": "Black",
            "price": 15000
        }
    },
    {
        "id": 11,
        "title": "Televisor Samsung",
        "description": "device with screen",
        "parameters": {
            "diagonal": 54,
            "technologies": "QLED",
            "color": "Black",
            "price": 35000
        }
    },

Получить детали товара : http://127.0.0.1:8000/api/product/id(например,http://127.0.0.1:8000/api/product/9)
получаете
{
    "id": 9,
    "title": "Televisor LG",
    "description": "device with screen",
    "parameters": {
        "diagonal": 24,
        "technologies": "LED",
        "color": "Black",
        "price": 15000
    }
}
