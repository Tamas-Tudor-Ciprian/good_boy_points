WIDTH = 1000

HEIGHT = 500

BLACK = (0,0,0)
GREY = (174,174,174)
BROWN= (196,98,16)
SKY_COLOR = (0, 255, 230)
CHARACTER_COLOR = (255, 179, 0)



def comp_dist (obj1,obj2,distance):
    return abs(obj1.x - obj2.x) <distance and abs(obj1.y-obj2.y) < distance