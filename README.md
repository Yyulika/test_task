# test_task
DJANGO

Необходимые шаги для инсталляции(pip install django,pip install pymongo,pip install djongo, pip install djangorestframework)
переходите в папку,где находится manage.py,чтобы сделать миграции и запуск сервера
перед запуском нужно сделать( manage.py makemigrations,затем manage.py migrate)
Команда для запуска(manage.py runserver)
Curl-команды:
На Windows я писала следующее в командной строке:
Для создания товара:

curl --location --request POST "http://127.0.0.1:8000/api/product/create/" --header "Content-Type: application/json" --data-raw "{ \"title\": \"HeadphonesLG\", \"description\": \"deviceforlistentomusic\",\"parameters\":{ \"type\":\"info\"}}"
Результат выполнения: {"id":30,"title":"HeadphonesLG","description":"deviceforlistentomusic","parameters":{"type":"info"}}

Для показа всех товаров:
curl --location --request GET "http://127.0.0.1:8000/api/products/"
Результат выполнения:
[{"id":29,"title":"Headphons LG","description":"device for listen to music","parameters":{"color":"black","power":"-"}},{"id":30,"title":"HeadphonesLG","description":"deviceforlistentomusic","parameters":{"type":"info"}},{"id":31,"title":"HeadphonesLG","description":"deviceforlistentomusic","parameters":{"type":"C"}}]


Для показа деталей по id:
curl --location --request GET "http://127.0.0.1:8000/api/product/29/"
Результат выполнения {"id":29,"title":"Headphons LG","description":"device for listen to music","parameters":{"color":"black","power":"-"}}

Для поиска по параметрам:
curl --location --request GET "http://127.0.0.1:8000/api/products/?search=Black"
Результат выполнения: [{"id":29,"title":"Headphons LG","description":"device for listen to music","parameters":{"color":"black","power":"-"}},{"id":32,"title":"SmartphonesLG","description":"deviceforlistentomusic","parameters":{"color":"Black"}}]

Также я тестировала url через Postman

Для создания товара : http://127.0.0.1:8000/api/product/create/
в поле для создания прописываете,например 
{"title": "Headphones SVEN ",
        "description": "device for listen to music",
        "parameters": {
            "connection": "wired",
            "power": "-",
            "color": "Black"}
}

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
        "id": 29,
        "title": "Headphons LG",
        "description": "device for listen to music",
        "parameters": {
            "color": "black",
            "power": "-"
        }
    },
    {
        "id": 30,
        "title": "HeadphonesLG",
        "description": "deviceforlistentomusic",
        "parameters": {
            "type": "info"
        }
    },
    {
        "id": 31,
        "title": "HeadphonesLG",
        "description": "deviceforlistentomusic",
        "parameters": {
            "type": "C"
        }
    }
]
    

Для поиска по параметрам : http://127.0.0.1:8000/api/products/?search=15000
[
    {
        "id": 34,
        "title": "Smartphones Samsung",
        "description": "device for listen to music",
        "parameters": {
            "color": "white",
            "price": 15000
        }
    },
    {
        "id": 36,
        "title": "Televizor Samsung",
        "description": "device for listen to music",
        "parameters": {
            "color": "black",
            "price": 15000
        }
    }
]

Получить детали товара : http://127.0.0.1:8000/api/product/id(например,http://127.0.0.1:8000/api/product/36)
получаете
{
    "id": 36,
    "title": "Televizor Samsung",
    "description": "device for listen to music",
    "parameters": {
        "color": "black",
        "price": 15000
    }
}
