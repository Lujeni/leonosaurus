qa:
	pre-commit run -v --all-files --show-diff-on-failure

migrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

run: migrate
	python src/manage.py loaddata initial_test_user && \
	python src/manage.py runserver

sync-gitlab:
	python src/manage.py sync_gitlab

scan-report:
	python src/manage.py scan_report $1
