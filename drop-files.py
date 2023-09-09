# RUN with drop-files.py files files-to-not-drop.txt

import os
import sys

def readFileLines(filename):
    file = open(filename, 'r')
    data = file.read()
    list = data.split("\n")
    file.close()
    return list

def dropAllOtherFiles(rootpath, filename_exclusions: list, testMode = False):
    total_count = 0
    dropped_count = 0
    preserved_count = 0
    not_processed_files = filename_exclusions.copy()
    for dirpath, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            total_count = total_count + 1
            filepath = os.path.join(dirpath, filename)
            if filepath in filename_exclusions:
                not_processed_files.remove(filepath)
                preserved_count = preserved_count + 1
                print("Preserving:  " + filepath)
            else:
                dropped_count = dropped_count + 1
                #print("Dropping:  " + filepath)
                if testMode == False:
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    if os.path.isdir(filepath):
                        os.rmdir(filepath)
    
    print('')
    print('Total files:', total_count)
    print('Total preserved files:', preserved_count)
    print('Total dropped files:', dropped_count)
    print('Not processed files:', not_processed_files)

exclusions = readFileLines(sys.argv[2])
dropAllOtherFiles(sys.argv[1], exclusions, True)