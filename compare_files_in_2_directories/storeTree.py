import os
import json
import sys

def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield [os.path.join(baseDir, entry.name), entry.stat().st_size]
        else:
            yield from scanRecurse(entry.path)

whichDir = sys.argv[1]
outFilePath = sys.argv[2]

all_files = []
for file in scanRecurse(whichDir):
    all_files.append(file)
all_files = [[os.path.relpath(file[0], whichDir), file[1]] for file in all_files]

with open(outFilePath, 'w') as file:
    json.dump(all_files, file)