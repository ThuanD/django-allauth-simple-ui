.PHONY: init build migrate user run update-deps

init:
	poetry install --all-extras

build:
	poetry build

migrate:
	poetry run python testproject/manage.py migrate

user:
	poetry run python testproject/create_user.py -u user -p user

run:
	poetry run python testproject/manage.py runserver

update-deps:
	poetry update
