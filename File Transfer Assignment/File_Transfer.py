import shutil
import os
from os import *
from shutil import *

source = 'C:/Users/Cody/OneDrive/Documents/GitHub/Projects-in-Python/File Transfer Assignment/Folder A/'

destination = 'C:/Users/Cody/OneDrive/Documents/GitHub/Projects-in-Python/File Transfer Assignment/Folder B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
