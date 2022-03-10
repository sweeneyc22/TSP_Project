print('Hello.')
from Map_handler import Map_handler
from Guess_and_Check_Path_Finder import Guess_and_Check_Path_Finder

city_count = 9
#time_limit_in_seconds = 3
print(f'City count is {city_count}.')

print('Load map')
map_handler_object = Map_handler()
map_handler_object.load_map(city_count)

print('Generate path')
guess_and_check_path_finder = Guess_and_Check_Path_Finder(city_count)
guess_and_check_path_finder.find_path()

print('Get path distance')
