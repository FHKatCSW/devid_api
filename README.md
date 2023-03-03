# Flask API Sample

<br />

## ✨ API Definition

| Route  | Verb | Info | Status | 
|    --- | ---  | --- | --- | 
| `/datas`    | **GET**    | return all items  | ✔️ | 
|             | **POST**   | create a new item | ✔️ |
| `/datas:id` | **GET**    | return one item   | ✔️ | 
|             | **PUT**    | update item       | ✔️ |
|             | **DELETE** | delete item       | ✔️ |

<br />

## Docker config

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-api-sample.git
$ cd flask-api-sample
```

> Start the app in Docker

```bash
$ docker-compose up --build  
```

The API server will start using the PORT `5000`.

<br />

## Using the code

> **Step #1** - Clone the project

```bash
$ git clone https://github.com/app-generator/flask-api-sample.git
$ cd flask-api-sample
```

<br />

> **Step #2** - create virtual environment using python3 and activate it 

```bash
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

<br />

> **Step #4** - setup `flask`

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```
<br />

> **Step #5** - start test APIs server at `localhost:5000`

```bash
$ flask run --host=0.0.0.0 --port=5000
```

Swagger API documentation is available at http://YOUR_HOST_NAME:5000/v1/

<br />

## ✨ Project Structure

```bash
api-server-flask/
├── api
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── README.md
├── requirements.txt
└── run.py
```
<br />

---
**[Flask API Sample](https://appseed.us/boilerplate-code/flask-api-boilerplate)** - provided by AppSeed [App Generator](https://appseed.us)
