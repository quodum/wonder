import sys

from vader_routes import *


try:
    from routes import Mapper
except ImportError:
    print("This example requires Routes to be installed")


class Application(object):
    def __init__(self):
        self.map = Mapper()

        self.map.connect('vaderconnect', '/vader/connect', app=vaderconnect)
        self.map.connect('vaderstage', '/vader/stage', app=vaderstage)
        self.map.connect('vaderpres', '/vader/pres', app=vaderpres)
        self.map.connect('vaderwins', '/vader/wins', app=vaderwins)
        self.map.connect('vaderloses', '/vader/loses', app=vaderloses)
        self.map.connect('vaderrock', '/vader/rock', app=vaderrock)
        self.map.connect('vaderpaper', '/vader/paper', app=vaderpaper)
        self.map.connect('vaderstop', '/vader/stop', app=vaderstop)

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
