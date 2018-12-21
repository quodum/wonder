import time
from WonderPy.components.wwMedia import WWMedia
from wonderwars.robot import RobotConnection


class VaderRobot(RobotConnection):
    def appearance(self, robot):
        robot.commands.RGB.stage_front(0, 0, 1)
        robot.commands.RGB.stage_ear_left(0, 0, 0)
        robot.commands.RGB.stage_ear_right(0, 0, 0)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)

    def presents(self, robot):
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_08)

        # 4 ture
        for i in range(1,6):
            robot.commands.body.stage_wheel_speeds  (-7.8, 7.8)

    def wins(self, robot):
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)
        robot.commands.body.stage_wheel_speeds  (-25.56, 25.56)
        robot.commands.body.stage_wheel_speeds  (25, -25)

    def loses(self, robot):
        robot.commands.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)

    def rock(self, robot):
        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            robot.commands.head.stage_tilt_angle(15)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_02)

    def paper(self, robot):
        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            robot.commands.head.stage_tilt_angle(15)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_03)
