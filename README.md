# Book Microservice

Une simple architecture de microservice avec FastAPI


## Prérequis:

- Python 3.8+
- pipenv ou pip

##  Cloner le projet

```
git clone https://github.com/flavienn-hugs/fastapi-book-microservice.git
```

## Tester le projet en local

### Installer les dépendances

```Utilisateur de pipenv
pipenv install
```
ou
```Utilisateur de pip
pip install -r requirements.txt
```

### Exécuter le serveur

```
uvicorn main:app --reload
```

### Exécuter le test

```
pytest test.py
```

## Documentation sur l'API

```
http://127.0.0.1:8000/docs
```
