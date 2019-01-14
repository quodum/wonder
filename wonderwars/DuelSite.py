from threading import Thread
import time

import WonderPy.core.wwMain
from WonderPy.core.wwConstants import WWRobotConstants
from WonderPy.components.wwMedia import WWMedia
from pprint import pprint


"""
This example shows connecting to the robot and issuing some simple commands.
See the other 'tutorial' and 'misc' examples for more complex scenarios!
"""



class MyClass(object):

    def on_connect(self, robot):
        """
        Called when we connect to a robot. This method is optional. Do not Block in this method !
        """
        robot.cmds.RGB.stage_all(0.2, 0.2, 0.2)
        robot.commands.RGB.stage_front(0, 0, 0)
        robot.commands.RGB.stage_ear_left(0, 0, 0)
        robot.commands.RGB.stage_ear_right(0, 0, 0)
        
        #print("Starting a thread for %s." % (robot.name))
        #Thread(target=self.thread_yoda, args=(robot,)).start()
        Thread(target=self.thread_vader, args=(robot,)).start()

    def thread_rotate(self, robot):
        angle=45
        speed=30
        
        print(robot.sensors.distance_rear)
        robot.commands.body.do_turn(45, 30)



    def thread_yoda(self, robot):
        #50 cm between (robot front-scene middle)
        #yoda push vader out and come back to original position
        robot.commands.body.do_forward(40, 20)
        robot.commands.body.do_turn(-90, 40)
        time.sleep(5)
        robot.commands.body.do_turn(90, 40)
        robot.commands.body.do_forward(35, 20)
        robot.commands.body.do_forward(-30, 10)
        #robot.commands.body.do_wheel_speeds(-30, 30)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)
        robot.commands.body.do_turn(-1100, 150)
        robot.commands.body.do_forward(45, 10)
        robot.commands.body.do_turn(180, 40)
        
        #code for yoda being pushed(coming from the left side of the scene-viewers side)
        #50 cm-Distance between robot front and middle of the scene frame
        robot.commands.body.do_forward(40, 20)
        robot.commands.body.do_turn(-90, 40)
        time.sleep(5)
        robot.commands.body.do_turn(90, 40)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)
        robot.commands.body.do_forward(-40, 30)

        
        #self.turnL(robot)
        #self.turn90(robot)
    
    def thread_vader(self, robot):
    
        """
        #50 cm between (robot front-scene middle)
        #vader push yoda
        robot.commands.body.do_forward(40, 20)
        robot.commands.body.do_turn(90, 40)
        time.sleep(5)
        robot.commands.body.do_turn(-90, 40)
        robot.cmds.head.stage_tilt_angle(15)
        robot.commands.body.do_forward(35, 10)
        robot.commands.body.do_forward(-20, 10)
        #robot.commands.body.do_wheel_speeds(-30, 30)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)
        robot.commands.body.do_turn(540, 90)
        #time.sleep(1)
        robot.commands.body.do_forward(55, 10)
        robot.commands.body.do_turn(180, 30)
        """
        #code for opponent being pushed(entering right side)
        robot.commands.body.do_forward(40, 20)
        robot.commands.body.do_turn(90, 40)
        time.sleep(5)
        robot.commands.body.do_turn(-90, 40)
        robot.cmds.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)
        time.sleep(1)
        robot.commands.body.do_forward(-40, 10)
        
    


    def turn90(self,robot):
        #d1=robot.sensors.distance_front_left_facing._distance_approximate
        #d2=robot.sensors.distance_front_right_facing._distance_approximate
        y = 0
        

        
            #robot.commands.body.do_forward(100, 30)
            #robot.commands.body.do_turn(180, 60)
            #d1=robot.sensors.distance_front_left_facing._distance_approximate
            #d2=robot.sensors.distance_front_right_facing._distance_approximate
            #print(y)
            #y = y + 1

        """
            if d1+d2 3:
                break
            i += 1
            y = 5 y=i-1 >0"""
    
    def robot_position(position):
        position = (x,y)
        return robot.position
        print(position)

        #if d1+d2>30:
         #   robot.commands.body.do_turn(-180, 40)
          #  print (d1,d2)

        #robot.commands.body.stage_wheel_speeds_naive(30, -30)

        robot.commands.body.do_turn(-90, 30)
        self.turn90(robot)
        robot.commands.body.stage_stop()
        #robot.commands.body.do_forward(20, 7)
        
        

    """def turnL(self, robot):
        # .distance_approximate()
        d1=robot.sensors.distance_rear._distance_approximate
        #robot.commands.body.do_turn(2, 40)
        #pprint(vars(d1))
        robot.commands.body.stage_wheel_speeds (5, -5)
        time.sleep(100)
        d2=robot.sensors.distance_rear._distance_approximate
        robot.commands.body.stage_wheel_speeds (0, 0)
        print("L", d1, d2)
        if d2 == 50 or d2 == None or d1 == None:
            self.turnL(robot)
            return
        if d2>d1:
            self.turnR(robot)
            return
        if d2<d1:
            self.turnL(robot)
            return
        print("Le: ", d2)

    def turnR(self, robot):
        d1=robot.sensors.distance_rear._distance_approximate
        #robot.commands.body.do_turn(-2, 40)
        #pprint(vars(d1))
        robot.commands.body.stage_wheel_speeds (-5, 5)
        time.sleep(100)
        d2=robot.sensors.distance_rear._distance_approximate
        robot.commands.body.stage_wheel_speeds (0, 0)
        print("R", d1, d2)
        
        if d2 == 50 or d2 == None or d1 == None:
            self.turnR(robot)
            return
        if d2>d1:
            self.turnL(robot)
            return
        if d2<d1:
            self.turnR(robot)
            return
        print("Re: ", d2) 
    """



    def wall2(self, iter, robot, angle, speed):
        print(iter)
        if iter == 0:
            return
        
        self.wall2(iter-1,robot)

    #def thread_angle():

    def rotate(self, robot, speed, angle):
        robot.commands.body.do_turn(45, 30)



    def thread_hello(self, robot):
        # robot is the robot we've connected to.

        # get a short list of sounds to play for this robot
        sound_names = self.get_hello_sounds(robot)

        for sound_name in sound_names:
            # for each sound in the list: turn on the lights, play the sound, dim the lights, then pause a little.
            print("On robot %s, setting all RGB lights to white." % (robot.name))
            robot.cmds.RGB.stage_all(1, 1, 1)

            print("On robot %s, playing '%s'." % (robot.name, sound_name))
            robot.cmds.media.do_audio(sound_name)

            print("On robot %s, setting all RGB lights to dim." % (robot.name))
            robot.cmds.RGB.stage_all(0.2, 0.2, 0.2)

            print("Waiting a little bit.")
            time.sleep(3)

        print("On robot %s, setting all RGB lights to off." % (robot.name))
        robot.cmds.RGB.stage_all(0, 0, 0)
        print("That's all for now.")

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



# kick off the program !
if __name__ == "__main__":
    WonderPy.core.wwMain.start(MyClass())
