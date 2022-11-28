# Book Microservice

Une simple architecture de microservice avec FastAPI


## Prérequis:

- Python 3.8+
- pipenv ou pip
- Docker && Docker Compose

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

### Construire le container avec docker

```
make docker-compose-up
```

## Documentation sur l'API

```Endpoint authors
http://localhost:8080/api/v1/authors/docs
```

```Endpoint books
http://localhost:8080/api/v1/books/docs
```
