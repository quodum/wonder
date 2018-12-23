from threading import Thread
import time
import json
import os

import WonderPy.core.wwMain
import WonderPy.core.wwBTLEMgr
from WonderPy.core.wwConstants import WWRobotConstants
from WonderPy.components.wwMedia import WWMedia


class Robot():
    def __init__(self, db_file_name, RobotType):
        self.conn = RobotType(db_file_name)

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
        # print('on_sensors self.robot', self.robot)
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
