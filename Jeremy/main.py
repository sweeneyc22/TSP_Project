#print('Hello.')
from Map_handler import Map_handler
from Guess_and_Check_Path_Finder import Guess_and_Check_Path_Finder

city_count = 9
time_limit_in_seconds = 20
#print(f'City count is {city_count}.')

#print('Load map')
map_handler_object = Map_handler(city_count)
map_handler_object.load_map()

#print('Generate path')
guess_and_check_path_finder = Guess_and_Check_Path_Finder(city_count)
guess_and_check_path_finder.find_path()

#print('Get path distance')
path_distance = map_handler_object.get_path_distance(guess_and_check_path_finder.get_path())
print(f'path distance: {path_distance}. ', end = '')
print(guess_and_check_path_finder.get_path())

guess_and_check_path_finder.run_guess_and_check_algorithm(map_handler_object, time_limit_in_seconds)
