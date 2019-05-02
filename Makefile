pylint:
	isort --recursive wagtail_tuto --skip project_dir/wsgi.py --skip-glob "*/migrations/*" --skip-glob "*/node_modules/*"
	flake8 wagtail_tuto
