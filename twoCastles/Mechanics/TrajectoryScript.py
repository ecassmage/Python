"""
If sprite.hold is True then the Catapult will not reduce its firing speed and will instead go at its proper
power level to achieve optimal distance. Currently I just need to implement a catapult object and the finish
off the Catapult Payload object then finish developing a bit more of the background logic to finish off the
firing arc to complete this ensemble.
"""
import math
from classes import projectiles
import json
settings = json.load(open('E:/Github/Python/twoCastles/settings.json', 'r'))


class Temp:
    def __init__(self):
        self.speed = 25/60


def make_new_rock(catapult_obj, dst, target):
    if catapult_obj.team == 'blue':
        dst -= target.scale
    else:
        dst += target.scale
    if target.can_move:
        spd, dst = completed_arc(dst, target)
    else:
        spd = speed_of_arc(dst)
    return projectiles.CatapultBall(catapult_obj.window, spd, catapult_obj.team,
                                    catapult_obj.x, catapult_obj.y, dst)


def arc_movement(arc_object):
    arc_object.y_arc -= arc_object.gravity
    arc_object.xy = (arc_object.x, arc_object.y)
    arc_object.xy_arc = (arc_object.x_arc, arc_object.y_arc)
    if -5 <= arc_object.y - arc_object.y_start <= 5 and not (-10 <= arc_object.x_start <= 10):
        explosion()


def explosion():
    """This will deal with the explosion that shall take place."""
    pass


def speed_of_arc(distance_x):
    """
    If I cheat and retain something like a 45 degree angle at all times I can calculate time it takes to fall easier
    If I want to go 600m, I need to arc it too 300m, that is all it will fall to 600m that way
    80/s
    y = speed * math.sin(math.pi/4)
    t = -y/9.8
    (((speed * math.sin(math.pi/4))/9.8)*2)(80(math.cos(math.pi/4)))
    """
    # speed = 80
    # distance_x = ((((speed * math.sin(math.pi/4))/9.8)*2) * (80) * (math.cos(math.pi/4)))
    # (distance_x / (math.cos(math.pi / 4))) = ((((speed * math.sin(math.pi / 4)) / 9.8) * 2) * speed)
    # (distance_x / (math.cos(math.pi / 4))) * (9.8 / (2 * math.sin(math.pi/4))) = speed**2
    # speed = math.sqrt((distance_x / (math.cos(math.pi / 4))) * (9.8 / (2 * math.sin(math.pi/4))))
    speeds = math.sqrt(abs((distance_x / (math.cos(math.pi / 6))) *
                           (settings['game']['gravity'] / (2 * math.sin(math.pi/6)))))
    """This is how fast it needs to be"""
    # print(speeds)
    return speeds


def time_of_arc(speeds):
    return ((speeds * math.sin(math.pi / 6)) / settings['game']['gravity']) * 2
    # Give or take 11 seconds
    # Target moves at 25 pixels/second
    # 660 pixels


def reduced_distance(tme, dst, spd):
    spd *= settings['fps']
    return (dst - (tme * spd)) * (dst - (tme * spd)) / dst


def completed_arc(distance_away, target):
    speed_of_shot = speed_of_arc(distance_away)
    time_change = time_of_arc(speed_of_shot)
    new_dist = reduced_distance(time_change, distance_away, target.speed)
    return speed_of_arc(new_dist), new_dist


# print(time_of_arc(speed_of_arc(600)))
# speed_of_arc(700)
# speed_of_arc(456)
# speed_of_arc(123)
# speed_of_arc(345)
# completed_arc(600, Temp())
