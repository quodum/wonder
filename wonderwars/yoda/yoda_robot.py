import time
from WonderPy.components.wwMedia import WWMedia
from wonderwars.robot import RobotConnection


class YodaRobot(RobotConnection):
    # def on_sensors(self, robot):
    #     # Robot.on_sensors(self, robot)
    #     super(YodaRobot, self).on_sensors(robot)

    def appearance(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            time.sleep(0.5)
            robot.commands.head.stage_tilt_angle(15)
            time.sleep(0.5)

    def presents(self, robot):
        robot.commands.RGB.stage_front(0, 0, 0)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)


        # 4 ture
        for i in range(1,6):
            robot.commands.body.stage_wheel_speeds (-7.8, 7.8)
            time.sleep(1.87)

        #robot.commands.body.stage_stop()

    def wins(self, robot):
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

    def loses(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        robot.commands.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)
        #robot.commands.body.stage_stop()

    def rock(self, robot):
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

    def paper(self, robot):
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)
        robot.commands.RGB.stage_front(0, 0, 0)

        time.sleep(5)

        for i in range(1,4):
            robot.commands.head.do_tilt_angle(-15)
            time.sleep(0.5)
            robot.commands.head.do_tilt_angle(15)
            time.sleep(0.5)

        robot.cmds.media.do_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_03)
