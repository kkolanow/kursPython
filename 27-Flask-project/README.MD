https://flask.palletsprojects.com/en/2.0.x/quickstart/

set FLASK_APP=hello
set FLASK_ENV=development
flask run

## Git bash
export FLASK_APP=hello
flask run

## Test curl
curl -d "user=user1&pass=abcd" -X POST https://example.com/login

curl -X GET http://127.0.0.1:5000/piotr
curl -X POST -H "imie: piotr" http://127.0.0.1:5000/piotr

1. zmiana poziomu logowania na ERROR . co sie zmienia w logach?
2. zmiana poziomu logowania na DEBUG . co sie zmienia w logach?

3. GET / - pobranie wszystkich persons 
4. GET /{number} - pobranie person po id (numer z listy) 
5. POST - dodanie osoby 
6. PUT - zmiana imienia osoby 
7. DELETE - usuniecie osoby
PATCH

## bledy 
abort(401)
