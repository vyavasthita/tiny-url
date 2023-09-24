NAME := Url Shortner
REPO_URL=https://github.com/vyavasthita/tiny-url
BUILD_ENV ?= development
.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Welcome to $(NAME)!"
	@echo "Use 'make <target>' where <target> is one of:"
	@echo ""
	@echo "  all		run stop -> up"
	@echo "  test		run test"
	@echo "  testv		run automated tests with standard output"
	@echo "  testcov	run testcov"
	@echo "  clean		clear network, container and images"
	@echo "  build		build container images"
	@echo "  up		run containers"
	@echo "  start		start containers"
	@echo "  restart	restart containers"
	@echo "  restartapp	restart app container"
	@echo "  stop		stop containers"
	@echo "  cdb		Connect to db container"
	@echo "  capp		Connect to app container"
	@echo "  down		bring down containers"
	@echo "  logs		show logs of containers"
	@echo "  ps		show container status"
	@echo "  destroy	destroy containers"
	@echo ""
	@echo "Choose one option!"

ifeq ($(BUILD_ENV),qa)
 $(info qa)
 ENV_FILE=app/configuration/qa/.env.app
 COMPOSE_FILE=docker-compose.qa.yaml
else ifeq ($(BUILD_ENV), production)
$(info production)
 ENV_FILE=app/configuration/production/.env.app
 COMPOSE_FILE=docker-compose.prod.yaml
else
 $(info development)
 ENV_FILE=app/configuration/development/.env.app
 COMPOSE_FILE=docker-compose.dev.yaml
endif

TEST_ENV_FILE=app/configuration/.env.test

test: test
testcov: testcov
all: stop up

.PHONY: clean
clean: ## clear network, container and images
	docker network prune -f
	docker container prune -f
	docker image prune -f
.PHONY: build
build: ## build container images
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) build --no-cache
.PHONY: up
up: ## run containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d --build --remove-orphans
.PHONY: start
start: ## start containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) start
.PHONY: restart
restart: ## restart containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d
.PHONY: restartapp
restartapp: ## restart containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) restart url-shortner-development
.PHONY: stop
stop: ## stop containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop
.PHONY: cdb
cdb: ## cdb
	docker exec -it cassandra-db-development cqlsh
.PHONY: capp
capp: ## capp
	docker exec -it url-shortner-development sh
.PHONY: down
down: ## bring down containers
	docker compose down
.PHONY: logs
logs: ## show logs of containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) logs
.PHONY: ps
ps: ## show container status
	docker ps -a
.PHONY: destroy
destroy: ## destroy containers
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down -v
.PHONY: test
test: ## run unit tests
	docker exec -e RUN_ENV=test url-shortner-$(BUILD_ENV) pytest -v
testv: ## run unit tests with standard output on console
	docker exec -e RUN_ENV=test url-shortner-$(BUILD_ENV) pytest -s
.PHONY: testcov
testcov: ## run unit tests overage report
	docker exec -e RUN_ENV=test url-shortner-$(BUILD_ENV) pytest --cov