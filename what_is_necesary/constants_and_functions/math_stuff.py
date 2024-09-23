def comp_dist (obj1,obj2,distance):
    return abs(obj1.x - obj2.x) < distance and abs(obj1.y-obj2.y) < distance + distance / 2