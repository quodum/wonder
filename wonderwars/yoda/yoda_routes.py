import sys
import os
from wsgiref.validate import validator
from gunicorn import __version__

from yoda_robot import YodaRobot
from wonderwars.robot import Robot


dir_path = os.path.dirname(os.path.realpath(__file__))
db_file = dir_path + '/yoda.json'

Yoda = Robot(db_file, YodaRobot)


@validator
def yodaconnect(environ, start_response):
    """Simplest possible application object"""

    data = b'Hello, World!\n'
    status = '200 OK'

    sys.argv = ['serve.py', '--connect-type', 'dash', '--connect-name', 'Yoda']

    global Yoda
    Yoda.start()

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodastage(environ, start_response):
    """Simplest possible application object"""

    data = 'appearance'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["appearance"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodastop(environ, start_response):
    """Simplest possible application object"""

    data = 'stop'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["stop"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodapres(environ, start_response):
    """Simplest possible application object"""

    data = 'presents'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["presents"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])

@validator
def yodawins(environ, start_response):
    """Simplest possible application object"""

    data = 'wins'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["wins"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodaloses(environ, start_response):
    """Simplest possible application object"""

    data = 'loses'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["loses"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodarock(environ, start_response):
    """Simplest possible application object"""

    data = 'rock'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["rock"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def yodapaper(environ, start_response):
    """Simplest possible application object"""

    data = 'paper'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["paper"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])

@validator
def yodascissors(environ, start_response):
    """Simplest possible application object"""

    data = 'scissors'
    status = '200 OK'

    with open(db_file, "w") as commands_file:
        commands_file.write('{"staged":["scissors"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])
