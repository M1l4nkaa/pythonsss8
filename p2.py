from sense_het import SenseHat
import math
import time

sense = SenseHat()
sense.clear()

meret = 8

ox = 3
oy = 3

lc = (0, 255, 0)   
pc = (255, 0, 0)    
bg = (0, 0, 0)

start_orientation = sense.get_orientation()
start_yaw = start_orientation["yaw"]

def draw_arrow(angle_deg):
    sense.clear(bg)

    angle = math.radians(angle_deg)

    dx = math.cos(angle)
    dy = math.sin(angle)

    points = []

    for i in range(1, 5):
        x = int(round(ox + dx * i))
        y = int(round(oy - dy * i))

        if 0 <= x < meret and 0 <= y < meret:
            points.append((x, y))

    for p in points[:-1]:
        sense.set_pixel(p[0], p[1], lc)

    if points:
        tip = points[-1]
        sense.set_pixel(tip[0], tip[1], pc)

    sense.set_pixel(ox, oy, (0, 0, 255))


while True:
    orientation = sense.get_orientation()
    yaw = orientation["yaw"]

    delta_yaw = yaw - start_yaw

    draw_arrow(delta_yaw)

    time.sleep(0.1)
