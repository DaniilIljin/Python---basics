"""EX14."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter  how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    print(robot.get_position())
    robot.set_wheels_speed(32)
    robot.sleep(1)
    print(robot.get_position())
    robot.set_wheels_speed(32)
    robot.sleep(1)
    print(robot.get_position())
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while True:
        if 0 in robot.get_line_sensors():
            robot.set_wheels_speed(25)
            robot.sleep(0.5)
            robot.set_wheels_speed(0)
            robot.done()
            break
        print(robot.get_position())
        robot.set_wheels_speed(13)
        robot.sleep(0.7)
        print(robot.get_position())


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    print(robot.get_position())
    robot.set_wheels_speed(100)
    robot.sleep(1)
    for i in range(170):
        if robot.get_left_line_sensor() == robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(100)
            robot.sleep(0.05)
            print(robot.get_position())
        elif robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() == 0:
            robot.set_left_wheel_speed(50)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.05)
            print(robot.get_position())
            robot.set_wheels_speed(100)
            robot.sleep(0.05)
            print(robot.get_position())
        elif robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() != 0:
            robot.set_left_wheel_speed(100)
            robot.set_right_wheel_speed(50)
            robot.sleep(0.05)
            print(robot.get_position())
            robot.set_wheels_speed(100)
            robot.sleep(0.05)
            print(robot.get_position())
        elif robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0:
            robot.set_wheels_speed(-100)
            robot.sleep(0.1)
            print(robot.get_position())
            robot.set_left_wheel_speed(0)
            robot.set_right_wheel_speed(58)
            robot.sleep(0.5)
            if robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0:
                robot.set_left_wheel_speed(0)
                robot.set_right_wheel_speed(-58)
                robot.sleep(0.5)
                print(robot.get_position())
                robot.set_left_wheel_speed(0)
                robot.set_right_wheel_speed(58)
                robot.sleep(1)
                print(robot.get_position())
            if robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0:
                robot.set_left_wheel_speed(0)
                robot.set_right_wheel_speed(-58)
                robot.sleep(1)
                print(robot.get_position())
                break
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == '__main__':
    robot = FollowerBot(track_image='track.png', start_x=162, start_y=306)
    follow_the_line(robot)
