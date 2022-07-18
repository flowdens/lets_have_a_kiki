import time
from itertools import cycle


class TrafficLight:
    __color = None

    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    workflow = {RED: 7, YELLOW: 2, GREEN: 5}

    def running(self):
        for color, delay in cycle(self.workflow.items()):
            self.__color = color
            print(color)
            time.sleep(delay)


tl = TrafficLight()
tl.running()
