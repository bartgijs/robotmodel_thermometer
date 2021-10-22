# source: https://stackoverflow.com/a/60772438

import math


class Sensor:

    def __init__(self):
        self.time = 0
        self.min = 20
        self.range = 15
        self.delta = 0.07

    def measure(self):
        temperature = math.sin(2 * self.delta * self.time) + \
            math.sin(math.pi * self.delta * self.time)
        self.time += 1
        return self.min + self.range * temperature


def test():
    sensor = Sensor()
    for t in range(60):
        print("{}\t{}".format(t, sensor.measure()))


if __name__ == "__main__":
    test()
