import os
import sys

video_extensions = ['avi', 'mkv', 'mpeg', 'mpg', 'mp4', 'webm', 'm3u8', 'flv', 'wmv', 'mov']
def isVideoFormat(filename):
    return None != getVideoFormat(filename)

def getVideoFormat(filename):
    for videoFormat in video_extensions:
        if (filename.endswith('.' + videoFormat)):
            return videoFormat
        if (filename.endswith('.' + videoFormat.lower())):
            return videoFormat
        if (filename.endswith('.' + videoFormat.upper())):
            return videoFormat
    return None

def flattern_video_folders(rootpath, testmode = False):
    for dirpath, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            if dirpath == rootpath:
                continue
            if (isVideoFormat(filename)):
                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    targetfilepath = os.path.join(rootpath, filename)
                    print('Moving file ', filepath, ' to ', targetfilepath)
                    if not testmode:
                        os.rename(filepath, targetfilepath)
                if os.path.isdir(filepath):
                    print('Removing folder:', filepath)
                    if not testmode:
                        os.rmdir(filepath)

flattern_video_folders(sys.argv[1], False)
