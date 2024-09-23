import os


def get_all_paths(root_directory):
    path_list = os.listdir(root_directory)
    return path_list




root_directory = r"C:\Users\uig60821\PycharmProjects\good_boy_points\what_is_necesary\player_sprites"

path_list = os.listdir(r"C:\Users\uig60821\PycharmProjects\good_boy_points\what_is_necesary\player_sprites")

print(path_list)