import os
import re
import sys

video_extensions = ['avi', 'mkv', 'mpeg', 'mpg', 'mp4', 'webm', 'm3u8', 'flv', 'wmv', 'mov']
video_tokens = ['www.', 'DVD', 'DVD.Screener','DVD-Screener', 'DVDScreener', 'M1080', '760p', '1080p', 'BDR1080', 'BR-Screener', 'BRScreener', 'BR.Screener', 'BR.SCreener', 'HDTV.Screener', 'HDTV-Screener', 'HDTVScreener', 'HD.RD', 'XviD', 'MicroHD', 'HDRip', 'BRRip', 'DVDrip', 'HDR','BluRay']

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


def renameVideoFile(filename:str):
    videoformat = getVideoFormat(filename)
    if None == videoformat:
        return False
    pathindex = 0
    try:
        pathindex = filename.rindex('/')
    except:
        pass
    pathname = filename[0:pathindex]
    videoname = filename[pathindex:len(filename) - len(videoformat) - 1]
    targetname = renameFromTokens(videoname)
    targetname = renameMetadata(targetname)
    targetname = renameVideoTokens(targetname)
    targetname = renameCamelCase(targetname)
    targetname = targetname.strip()
    targetname = targetname.replace('  ', ' ')
    targetname = targetname.replace('   ', ' ')
    targetname = targetname.replace('    ', ' ')
    targetname = pathname + targetname + '.' + videoformat
    if videoname == targetname:
        return False
    print(filename, ' ==> ', targetname)
    # TODO: Do FS work:
    # os.rename(filename, targetname)
    return True


def renameCamelCase(videoname:str):
    return ' '.join(camelCaseSplit(videoname))

def camelCaseSplit(s):
    result = list()
    start = 0
    for i, c in enumerate(s[1:], 1):
        if c.isupper():
            if i > 0 and (s[i - 1].islower() or s[i - 1].isnumeric()):
                result.append(s[start:i].strip())
                start = i
    result.append(s[start:].strip())
    return result

def renameFromTokens(videoname:str):
    videonamelen = len(videoname)
    indexes = [videonamelen]
    try:
        indexes.append(videoname.index('[') - 1)
    except:
        pass
    try:
        indexes.append(videoname.index('(') - 1)
    except:
        pass
    for token in video_tokens:
        try:
            indexes.append(videoname.index(token))
        except:
            pass
    index = min(indexes)
    if index < 0:
        index = len(videoname)
    return videoname[0:index]

def renameMetadata(videoname:str):
    videoname = re.sub('\[.*\]', '', videoname)
    videoname = re.sub('\(.*\)', '', videoname)
    videoname = re.sub('\.', ' ', videoname)
    return videoname

def renameVideoTokens(videoname:str):
    for token in video_tokens:
        videoname = re.sub(token, '', videoname)
        videoname = re.sub(token.lower(), '', videoname)
        videoname = re.sub(token.upper(), '', videoname)
    return videoname



def renameVideos(filepaths:list):
    count = 0
    not_processed = list()
    for line in filepaths:
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        if renameVideoFile(line):
            count += 1
        else:
            not_processed.append(line)
    print('*******************************************************************************************')
    print('TOTAL renamed video files: ', count)
    #print('NOT processed files: ')
    #print('\n'.join(not_processed))

def renameVideosInFolder(rootpath:str):
    result = []
    for dirpath, dirnames, filenames in os.walk(rootpath):
        for filename in filenames:
            if (isVideoFormat(filename)):
                result.append(os.path.join(dirpath, filename))
    if len(result) > 0:
        renameVideos(result)

def renameVideosInFile(filepath:str):
    if filepath.endswith('.txt'):
        file = open(filepath, 'r')
        renameVideos(file.readlines())

if len(sys.argv) == 1:
    renameVideosInFolder('examples/')

if len(sys.argv) > 1:
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        renameVideoFile(filepath)
    else:
        if os.path.isdir(filepath):
            renameVideosInFolder(filepath)
        else:
            if isVideoFormat(filepath):
                renameVideoFile(filepath)
            else:
                renameVideosInFile(filepath)
