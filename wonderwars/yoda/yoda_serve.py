import sys

from yoda_routes import *


try:
    from routes import Mapper
except ImportError:
    print("This example requires Routes to be installed")


class Application(object):
    def __init__(self):
        self.map = Mapper()

        self.map.connect('yodaconnect', '/yoda/connect', app=yodaconnect)
        self.map.connect('yodastage', '/yoda/stage', app=yodastage)
        self.map.connect('yodapres', '/yoda/pres', app=yodapres)
        self.map.connect('yodawins', '/yoda/wins', app=yodawins)
        self.map.connect('yodaloses', '/yoda/loses', app=yodaloses)
        self.map.connect('yodarock', '/yoda/rock', app=yodarock)
        self.map.connect('yodapaper', '/yoda/paper', app=yodapaper)
        self.map.connect('yodastop', '/yoda/stop', app=yodastop)

    def __call__(self, environ, start_response):
        match = self.map.routematch(environ=environ)
        print('match', match)
        if not match:
            return self.error404(environ, start_response)
        return match[0]['app'](environ, start_response)

    def error404(self, environ, start_response):
        html = b"""\
        <html>
          <head>
            <title>404 - Not Found</title>
          </head>
          <body>
            <h1>404 - Not Found</h1>
          </body>
        </html>
        """
        headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(html)))
        ]
        start_response('404 Not Found', headers)
        return [html]

app = Application()
