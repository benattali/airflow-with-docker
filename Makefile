local-build:
	docker build -f ./Dockerfile .

start-postgres:
	docker-compose up -d postgres

start-webserver:
	docker-compose up -d webserver

local-run:
	$(MAKE) start-postgres
	$(MAKE) start-webserver
	@echo airflow running on http://localhost:8080

local-kill:
	@echo "Killing docker-airflow containers"
	docker-compose down