
from threading import Thread
import time
import sys
import json
import os


import math
from WonderPy.util import wwMath
import WonderPy.core.wwMain
import WonderPy.core.wwBTLEMgr
from WonderPy.core.wwConstants import WWRobotConstants
from WonderPy.components.wwMedia import WWMedia


class Robot():
    def __init__(self, db_file_name):
        self.conn = RobotConnection(db_file_name)

    def start(self):
        manager = WonderPy.core.wwMain.start(self.conn)
        print(manager)
        print(manager.robot)


class RobotConnection(object):
    def __init__(self, db_file_name):
        self.robot = None
        self._cached_stamp = 0
        self.db_file = db_file_name

    def on_connect(self, robot):
        """
        Called when we connect to a robot. This method is optional. Do not Block in this method !
        """
        self.robot = robot
        print('--- on_connect self.robot', self.robot)
        print("Starting a thread for %s." % (robot.name))

    def on_sensors(self, robot):
        """
        Called approximately 30 times per second - each time sensor data is received from the robot.
        This method is optional.
        Do not block in here !
        This means only call the stage_foo() flavor of robot commands, and not the do_foo() versions.
        """
        self.robot = robot
        # print('on_sensors self.robot', self.robot)
        # print("on_sensors %s." % (robot.name))
        # self.on_sensors_called += 1
        # if self.on_sensors_called == 1:
        print('on_sensors self.robot', self.robot)
        # print(os.stat(self.db_file))
        stamp = os.stat(self.db_file)[8] # .st_mtime
        print('stamp', stamp)
        if stamp != self._cached_stamp:
            print('read db')
            self._cached_stamp = stamp
            with open(self.db_file) as commands_file:
                commands = json.load(commands_file)["staged"]
            with open(self.db_file, "w") as commands_file:
                commands_file.write('{"staged":[]}')

            for command in commands:
                print('command', command)
                getattr(self, command)(robot)

    def hello(self):
        print('-------- hello self.robot', self.robot)
        Thread(target=self.thread_hello, args=(self.robot,)).start()

    def thread_hello(self, robot):
        # robot is the robot we've connected to.
        """
        print(u"%s waiting for button press." % (robot.name))
        robot.block_until_button_main_press_and_release()

        print(u"%s driving forward 20cm at 10cm/s." % (robot.name))
        """
        print('thread_hello')
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            time.sleep(0.5)
            robot.commands.head.stage_tilt_angle(15)
            time.sleep(0.5)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_03)

    def yoda_stage_present(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            time.sleep(0.5)
            robot.commands.head.stage_tilt_angle(15)
            time.sleep(0.5)

    def yoda_presents(self, robot):
        robot.commands.RGB.stage_front(0, 0, 0)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)


        # 4 ture
        for i in range(1,6):
            robot.commands.body.stage_wheel_speeds (-7.8, 7.8)
            time.sleep(1.87)

        #robot.commands.body.stage_stop()

    def yoda_wins(self, robot):
        robot.commands.RGB.stage_front(0, 0, 0)

        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)

        time.sleep(1)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)

        robot.commands.body.stage_wheel_speeds  (-35, 35)
        time.sleep(4.5)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)

        robot.commands.body.stage_wheel_speeds  (35, -35)
        time.sleep(4.5)
        #robot.commands.body.stage_stop()

    def yoda_loses(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        robot.commands.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)
        #robot.commands.body.stage_stop()

    def vader_stage_present(self, robot):
        robot.commands.RGB.stage_front(0, 0, 1)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)

        time.sleep(1)

    def vader_presents(self, robot):
        robot.commands.RGB.stage_front(0, 0, 1)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_08)

        # 4 ture
        for i in range(1,6):
            robot.commands.body.stage_wheel_speeds  (-7.8, 7.8)
            time.sleep(1.87)

        # robot.commands.body.stage_stop()

    def vader_wins(self, robot):
        robot.commands.RGB.stage_front(0, 0, 1)


        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)

        time.sleep(1)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)

        robot.commands.body.stage_wheel_speeds  (-25.56, 25.56)
        time.sleep(10)

        robot.commands.body.stage_wheel_speeds  (25, -25)

        # robot.commands.body.stage_stop()

    def vader_loses(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 255)

        time.sleep(5)


        robot.commands.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)
        # robot.commands.body.stage_stop()

    def yoda_rock(self, robot):
        # robot is the robot we've connected to.
        """
        print(u"%s waiting for button press." % (robot.name))
        robot.block_until_button_main_press_and_release()

        print(u"%s driving forward 20cm at 10cm/s." % (robot.name))
        """
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            time.sleep(0.5)
            robot.commands.head.stage_tilt_angle(15)
            time.sleep(0.5)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_02)

    def stop(self, robot):
        robot.commands.body.stage_stop()

    def get_hello_sounds(self, for_this_robot):
        # we don't know ahead-of-time if the robot will be a Cue, Dash, or Dot,
        # so we handle each of those cases now with an appropriate list of sounds to play:
        if for_this_robot.robot_type == WWRobotConstants.RobotType.WW_ROBOT_DASH:
            return [WWMedia.WWSound.WWSoundDash.HOWDY,
                    WWMedia.WWSound.WWSoundDash.HOWSGOING,
                    WWMedia.WWSound.WWSoundDash.LETS_GO,
                    ]

        elif for_this_robot.robot_type == WWRobotConstants.RobotType.WW_ROBOT_DOT:
            return [WWMedia.WWSound.WWSoundDot.HOWDY,
                    WWMedia.WWSound.WWSoundDot.HOLD_ME,
                    WWMedia.WWSound.WWSoundDot.READYSET,
                    ]

        elif for_this_robot.robot_type == WWRobotConstants.RobotType.WW_ROBOT_CUE:
            return [WWMedia.WWSound.WWSoundCue.zest_HEYWHSU,
                    WWMedia.WWSound.WWSoundCue.charge_BORESTNOC,
                    WWMedia.WWSound.WWSoundCue.pep_YOUSOGOT,
                    ]
        else:
            raise ValueError("unhandled robot type: %s on %s" % (str(for_this_robot.robot_type), for_this_robot.name))


try:
    from routes import Mapper
except ImportError:
    print("This example requires Routes to be installed")


Vader = Robot('vader.json')
Yoda = Robot('yoda.json')

from wsgiref.validate import validator
from gunicorn import __version__


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
def hello(environ, start_response):
    """Simplest possible application object"""

    print(environ, start_response)

    data = b'Hello, World!\n'
    status = '200 OK'

    with open("db.json", "w") as commands_file:
        commands_file.write('{"staged":["thread_hello"]}')

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

    data = 'yoda_presents'
    status = '200 OK'

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["yoda_presents"]}')

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

    data = 'yoda_wins'
    status = '200 OK'

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["yoda_wins"]}')

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

    data = 'yoda_loses'
    status = '200 OK'

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["yoda_loses"]}')

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

    data = 'vader_presents'
    status = '200 OK'

    with open("vader.json", "w") as commands_file:
        commands_file.write('{"staged":["vader_presents"]}')

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

    data = 'vader_wins'
    status = '200 OK'

    with open("vader.json", "w") as commands_file:
        commands_file.write('{"staged":["vader_wins"]}')

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

    data = 'vader_loses'
    status = '200 OK'

    with open("vader.json", "w") as commands_file:
        commands_file.write('{"staged":["vader_loses"]}')

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

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["stop"]}')

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

    with open("vader.json", "w") as commands_file:
        commands_file.write('{"staged":["stop"]}')

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

    data = 'yoda_stage_present'
    status = '200 OK'

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["yoda_stage_present"]}')

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

    data = 'vader_stage_present'
    status = '200 OK'

    with open("vader.json", "w") as commands_file:
        commands_file.write('{"staged":["vader_stage_present"]}')

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

    data = 'yoda_rock'
    status = '200 OK'

    with open("yoda.json", "w") as commands_file:
        commands_file.write('{"staged":["yoda_rock"]}')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__),
    ]
    start_response(status, response_headers)
    return iter([data])


class Application(object):
    def __init__(self):
        self.map = Mapper()
        # self.map.connect('connect', '/connect', app=connect)
        self.map.connect('hello', '/hello', app=hello)

        # self.map.connect('yodastage', '/yodastage', app=yodastage)
        # self.map.connect('yodapres', '/yodapres', app=yodapres)
        # self.map.connect('yodawins', '/yodawins', app=yodawins)
        # self.map.connect('yodaloses', '/yodaloses', app=yodaloses)
        # self.map.connect('yodarock', '/yodarock', app=yodarock)

        # self.map.connect('vaderstage', '/vaderstage', app=vaderstage)
        # self.map.connect('vaderpres', '/vaderpres', app=vaderpres)
        # self.map.connect('vaderwins', '/vaderwins', app=vaderwins)
        # self.map.connect('vaderloses', '/vaderloses', app=vaderloses)
        # self.map.connect('stop', '/stop', app=stop)

        self.map.connect('yodaconnect', '/yoda/connect', app=yodaconnect)
        self.map.connect('yodastage', '/yoda/stage', app=yodastage)
        self.map.connect('yodapres', '/yoda/pres', app=yodapres)
        self.map.connect('yodawins', '/yoda/wins', app=yodawins)
        self.map.connect('yodaloses', '/yoda/loses', app=yodaloses)
        self.map.connect('yodarock', '/yoda/rock', app=yodarock)
        self.map.connect('yodastop', '/yoda/stop', app=yodastop)

        self.map.connect('vaderconnect', '/vader/connect', app=vaderconnect)
        self.map.connect('vaderstage', '/vader/stage', app=vaderstage)
        self.map.connect('vaderpres', '/vader/pres', app=vaderpres)
        self.map.connect('vaderwins', '/vader/wins', app=vaderwins)
        self.map.connect('vaderloses', '/vader/loses', app=vaderloses)
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
