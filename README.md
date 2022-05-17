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

Since i'm using `Docker` with `docker-compose`, i can just do this:

```
docker-compose up -d
```

You need to **install** ``PSQL server`` if you don't have **docker** 

## Running the Project

Running django :

```
python ./manage.py runserver
```

you should see something like this :

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 17, 2022 - 08:36:09
Django version 4.0.3, using settings 'EpicEvents.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Then navigate to : http://127.0.0.1:8000/

> NOTE : if this isn't what you are seeing, and you are unable to access the website, then its probably because there is a typo somewhere or didn't follow the steps correctly ...

## Available Endpoints

There is few account available for testing, few posts has been already added for showcase

