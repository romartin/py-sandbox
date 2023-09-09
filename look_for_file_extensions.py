import os
import sys

def look_for_file_extensions(rootDir):
    extensions = set()
    for dirpath, dirnames, filenames in os.walk(rootDir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            exntesion_index= filepath.rindex(".")
            if exntesion_index > -1:
                extension = filepath[exntesion_index:]
                extensions.add(extension)
    print(extensions)
    
if len(sys.argv) > 1:
    look_for_file_extensions(sys.argv[1])
else:
    look_for_file_extensions('examples')