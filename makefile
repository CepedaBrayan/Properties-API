make-migrations:
	alembic revision --autogenerate -m "$(NAME)"

run-migrations:
	alembic upgrade head

start: run-migrations
	uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

run-test:
	pytest

# Local development
see-logs-local: start-local
	docker-compose logs -f

start-local:
	docker-compose up -d

stop-local:
	docker-compose down

restart-local: stop-local start-local

run-migrations-local: start-local
	docker-compose exec -it backend /bin/bash -c "alembic upgrade head"

make-migrations-local: start-local
	docker-compose exec -it backend /bin/bash -c "alembic revision --autogenerate -m '$(MIGRATION)'"

run-tests-local: start-local
	docker-compose run backend pytest