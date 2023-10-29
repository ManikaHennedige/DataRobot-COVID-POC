"""
This script runs the Ankspon application using a development server.
Make sure to change the port to 5000 if running via docker-compose, or 8080 if running purely with docker
"""

from os import environ
from App import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)