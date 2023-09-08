docker:
	docker-compose build && docker-compose up
pull:
	git pull origin main
static:
	python manage.py collectstatic
migrate:
	python manage.py migrate
spin:
	sudo systemctl restart gunicorn && sudo systemctl restart nginx
push:
	git add .
	git commit -m 'backend changes'
	git push