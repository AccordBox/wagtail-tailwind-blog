pylint:
	poetry run isort --recursive wagtail_tuto --skip project_dir/wsgi.py --skip-glob "*/migrations/*" --skip-glob "*/node_modules/*"
	poetry run flake8 wagtail_tuto
