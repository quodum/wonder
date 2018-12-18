import sys
import os
from wsgiref.validate import validator
from gunicorn import __version__

from vader_robot import VaderRobot
from wonderwars.robot import Robot


dir_path = os.path.dirname(os.path.realpath(__file__))
db_file = dir_path + '/vader.json'

Vader = Robot(db_file, VaderRobot)


@validator
def vaderconnect(environ, start_response):
    """Simplest possible application object"""

    data = b'Hello, World!\n'
    status = '200 OK'

    sys.argv = ['serve.py', '--connect-type', 'cue', '--connect-name', 'Vader']

    global Vader
    Vader.start()

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


@validator
def vaderstage(environ, start_response):
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
def vaderstop(environ, start_response):
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
def vaderpres(environ, start_response):
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
def vaderwins(environ, start_response):
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
def vaderloses(environ, start_response):
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
def vaderrock(environ, start_response):
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
def vaderpaper(environ, start_response):
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
