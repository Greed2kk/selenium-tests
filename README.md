# selenium-tests
Регрессионное тестирование на python selenium для niokr.rosseti-yug.ru

# развертка 
```
pipenv shell
pipenv install
```

# authTest
1. Создать файл ```data.json```
2. Положить туда json 
```json
{
    "url": "https://test12.ru/",
    "success": {
        "login": "admin12",
        "password": "131233"
    },
    "error": {
        "login": "admin13",
        "password": "1232131"
    }
    
}
```
3. Зупустить командой 
```
python auth_module.py -v
```


