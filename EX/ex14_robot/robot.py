"""EX14."""
from FollowerBot import FollowerBot


def run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter  how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(1)
    robot.sleep(1)
    robot.set_wheels_speed(0)
    robot.sleep(1)
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
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            robot.done()
            break
        robot.set_wheels_speed(10)
        robot.sleep(0.01)
        robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == '__main__':
    robot = FollowerBot()
    drive_to_line(robot)

