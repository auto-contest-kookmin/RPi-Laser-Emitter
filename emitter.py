import RPi.GPIO as GPIO
import time


class LaserModule(object):
    def __init__(self, channel):
        self._channel = channel

        # Setup GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._channel, GPIO.OUT)

    def laser_on(self):
        GPIO.output(self._channel, GPIO.HIGH)

    def laser_off(self):
        GPIO.output(self._channel, GPIO.LOW)

    def destroy(self):
        self.laser_off()
        GPIO.cleanup()


if __name__ == '__main__':
    lm = LaserModule(11)
    try:
        lm.laser_on()
        while True:
            print("0: LASER OFF\n1: LASER ON")
            n = int(input("Input: "))
            if n == 0:
                lm.laser_off()
            elif n == 1:
                lm.laser_on()
        
    except KeyboardInterrupt:
        lm.destroy()
