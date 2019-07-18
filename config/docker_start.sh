# Migrate database
python manage.py migrate

# run server
gunicorn config.wsgi:application
