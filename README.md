<p align="center">
    <img height="128" src="https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png">
</p>

> NOTE : `Python 3.9.9`, `Windows 11` & `Docker` was used while working on this project.

## Installation

We will need to create a virtual environment

```
python -m venv .venv
```

---

Then activate it

```
[WINDOWS]
./.venv/Scripts/activate

[LINUX]
source .venv/bin/activate
```

---

Once done, Install all the required dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Database

Since we are using `Docker` with `docker-compose`, we can just do this:

```
docker-compose up -d
```

You need to **install** ``PSQL server`` if you don't have **docker** 

> ### & be sure to check the .[env](./.env.example) file and update it accordingly.

### Database Diagram

![](.github%5CERD%20Diagram.png)

## Running the Project

before doing anything we will need to run the migrations 

> **be sure to have a valid DB connection first**

1. Running the migrations:

```
python manage.py migrate
```

2. Generate mockdata:
```
python manage.py gen_mock_data
```

3. Run django :

```
python ./manage.py runserver
```

When done, you should see something like this :

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 17, 2022 - 08:36:09
Django version 4.0.3, using settings 'EpicEvents.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

> NOTE : if this isn't what you are seeing, or you are unable to access the website/API, then its probably because there is a typo somewhere or didn't follow the steps correctly ...

## Tests

To make sure everythings works fine, you should run the tests using pytest:

```
pytest
```

You should have **43 passed** tests.

## Accounts

The command "gen_mock_data" will generate needed data for this project to work.

- Admin Credentials:
  - username : **admin**
  - password : **default**

> NOTE : All generated accounts credentials has the same password.

## API Documentation

### Errors

Errors you will encounter when using the endpoints below

**Response 400** when the given data is wrong/missing
```cs
"[field_name]": string[]
```

**Response 401** general info, bad creds/not authoized to access, etc
```cs
"detail": string
"code": string
```

### Available endpoints

- [Auth](./docs/Auth.md)
- [Client](./docs/Client.md)
- [Contract](./docs/Contracts.md)
- [Events](./docs/Events.md)
- [Users](./docs/Users.md)