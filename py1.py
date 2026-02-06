from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

white = (255, 255, 255)

for i in range(8):
    sense.set_pixel(i, i, white)