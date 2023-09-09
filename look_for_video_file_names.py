import os
import sys
import video_namings

def log_result(rootpath, videofilenames:set):
    print_set(videofilenames)
    file = open(rootpath + '/video_file_names.txt', 'w')
    for name in videofilenames:
        file.write(name + '\n')
    file.close()
    
def print_set(o:set):
    for i in o:
        print(i)

def look_for_video_file_names(rootpath):
    videofilenames = set()
    for dirpath, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            if video_namings.isVideoFormat(filename):
                videofilenames.add(filename)
    log_result(rootpath, videofilenames)
    
look_for_video_file_names(sys.argv[1])