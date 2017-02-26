from openalpr import Alpr
import inspect
import pprint

from os import walk

mypath = '/home/andrzej/Code/python/img'
files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    break

for file in files:
    if 'py' not in file:
        print(file)
        alpr = Alpr("gb", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
            sys.exit(1)

        alpr.set_top_n(20)
        alpr.set_default_region("gb")

        results = alpr.recognize_file(file)

        i = 0
        for plate in results['results']:
            pprint.pprint(plate)


# Call when completely done to release memory
alpr.unload()