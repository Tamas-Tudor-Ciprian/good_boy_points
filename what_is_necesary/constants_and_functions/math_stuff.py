def comp_dist (obj1,obj2,distance):
    return abs(obj1.x - obj2.x) < distance and abs(obj1.y-obj2.y) < distance + distance / 2

def comp_dist_tup (obj1,tup2,distance):
    return abs(obj1.x - tup2[0]) < distance and abs(obj1.y-tup2[1]) < distance


def find_element_and_continue(current_number,some_list):
    if current_number not in some_list:
        current_number = some_list[0]

    else:
        if current_number == some_list[-1]:
            current_number = some_list[0]

        else:
            current_number = some_list[some_list.index(current_number) + 1 ]

    return current_number