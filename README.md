# API Proxy Parser

* Этот проект имеет три части: ``pars.py``, ``check.py``, ``main.py``

### pars.py

* Этот файл имеет одну функцию ``parsing`` 
    * Задача этой функции спарсить IP, port, country proxy

### check.py
* Этот файл проверяет прокси на валидность
    * Для этого есть функция check. Функция посылает запрос на сайт и ожидает ответ, если ответа нет, то proxy невалидный

* Заносит proxy в базу данных
    * Я использую свою базу данных PyDB

### main.py
* Файл в котором лежит код сервера :)

## Как запустить?

* Установить все модули ``pip install -r requirements.txt``
* Запустить ``check.py``
* Запустить сервер ``uvicorn main:app``