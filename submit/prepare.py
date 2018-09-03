from os import listdir
from os.path import isfile, join

import shutil

test_file = open("test.csv", "w")

my_path = "/data/test/"

for f in listdir(my_path):
    if isfile(join(my_path, f)):
        test_file.write(f + "\n")

test_file.close()