from Lane import Lane

class Map:

    def __init__(self):
        Lane((0, 220), "green", width=3, height=31)
        Lane((0, 185), "red", width=0.4, height=31)
        Lane((0, 100), "green", width=1, height=31)
        (Lane((-290, 145), "white", 1, 1)).dash()
        Lane((0, 10), "green", width=1, height=31)
        (Lane((-290, 55), "white", 1, 1)).dash()
        Lane((0, -80), "green", width=1, height=31)
        (Lane((-290, -35), "white", 1, 1)).dash()
        Lane((0, -170), "green", width=1, height=31)
        (Lane((-290, -125), "white", 1, 1)).dash()
        Lane((0, -210), "green", width=3, height=31)
