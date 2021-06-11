# You are working on a new project on a client's computer. They need you to write some code that works with data from 4 different csvs. The following are the file paths for all of the csvs:

path_1 = "home/user/Gary/project/data.csv"
path_2 = "home/user/Gary/project2/data.csv"
path_3 = "home/user/Kayle/project/data.csv"
path_4 = "home/user/Kayle/project2/data.csv"

# So far, the client has the following code written. The code is used to move the csvs from all the various locations and move them to the destination path:

import shutil as s

destination_path = "home/user/Gary/newproject/"

s.move(path_1, destination_path)
s.move(path_2, destination_path)
s.move(path_3, destination_path)
s.move(path_4, destination_path)

# To make this code more reusable, enter all of the path data into the dictionary below, where the variable name (e.g. path_1, path_2) is the key and the path is the value. Then, rewrite the code above using the dictionary. No need to put the destination path into the dictionary.

paths_dict = {}

# Afterwards, copy and paste the line of code that you've updated that moves the csv located at path 4 into the quiz.