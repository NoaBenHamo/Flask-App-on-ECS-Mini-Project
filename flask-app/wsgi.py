# use this file and run the command 'gunicorn --bind 0.0.0.0:5000 wsgi:app'
# to check if it works manually

from app import app

if __name__ == '__main__':
    app.run()
