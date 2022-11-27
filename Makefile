MANAGE := python

PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	pipenv shell

.PHONY: install
install: venv ## Install or update dependencies
	pipenv install

.PHONY: freeze
freeze: ## Pin current dependencies
	pipenv requirements > requirements.txt
	cp Pipfile book_service/
	cp Pipfile author_service/

.PHONY: runserver
runserver: ## Run the server
	uvicorn author_service.app.main:app --reload

.PHONY: docker-compose-build
docker-compose-build: ## Build docker image
	docker-compose build

.PHONY: docker-compose-up
docker-compose-up: ## Execute docker image
	docker-compose up -d --build

.PHONY: docker-compose-down
docker-compose-down: ## Remove docker image
	docker-compose down

.PHONY: docker-compose-logs
docker-compose-logs: ## Check for errors in the logs if this doesn't work
	docker-compose logs -f

.PHONY: kill-process
kill-process: ## Kill process the server
	sudo lsof -t -i tcp:8000 | xargs kill -9
