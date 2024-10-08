import os



current_directory = os.getcwd()

wanted_location = current_directory +  "\\player\\player_sprites"


#print(wanted_location)
#print(os.listdir(wanted_location))



current_number = 4

some_list = [2,3,5,7,4]


def find_element_and_continue(current_number,some_list):
    if current_number not in some_list:
        current_number = some_list[0]

    else:
        if current_number == some_list[-1]:
            current_number = some_list[0]

        else:
            current_number = some_list[some_list.index(current_number) + 1 ]

    return current_number


print(find_element_and_continue(current_number,some_list))