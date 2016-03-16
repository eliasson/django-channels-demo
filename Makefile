all: init run

init:
	@pip install -r requirements.txt
	@python manage.py makemigrations demo
	@python manage.py migrate

run:
	@python manage.py runserver
