qa:
	pre-commit run -a

migrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

run: migrate
	python src/manage.py loaddata initial_test_user && \
	python src/manage.py runserver
