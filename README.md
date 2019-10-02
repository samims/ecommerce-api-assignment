# Ecommerce API

## Installation and run

Create virtualenv (Python3.6)
```bash
$ python3.6 -m venv myvenv
```
Activate virtualenv using
```bash
source myvenv/bin/activate
```
Clone this repo
```bash
git clone https://github.com/samims/ecommerce-api-assignment.git
```
Install dependencies
```bash
pip install -r requirements.txt
```
Go to the project directory and run migrations files  using this command
```bash
python manage.py migrate
```

To run this project
```bash
python manage.py runserver
```

To run tests
```bash
python manage.py test
```
# Documentation ecommerce API 

To create a user go to register API at ```http://127.0.0.1:8000/api/register/```
Sample payload
```bash
{
    "first_name": "test_user",
    "last_name: "dev"
    "username": "test",
    "email": "test@example.com",
    "password": "testpass"
}
```


To login navigate to ```/api/api-token-auth/```
Sample payload
```bash
{
    "username": "test",
    "password": "testpass"
}

```


It will return a token. Use that token in header to authenticate the user on other APIs

To verify and refresh token navigate to  ```http://127.0.0.1:8000/api/api-token-verify/``` and 
 ```http://127.0.0.1:8000/api/api-token-refresh/``` accordingly with following payload

```bash
{
    "token": "your token"
}
```


To find total product price in given categories
```bash
/api/sum/?categories=<comma separated id>
```

To get top users in terms of maximum number of order and max value order in last 30 days

```bash
http://127.0.0.1:8000/api/order/top-users/ 
``` 

To know further about api kindly follow the link

```bash
http://127.0.0.1:8000/api/docs