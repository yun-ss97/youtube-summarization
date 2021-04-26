## python -m pip install pytube

from pytube import YouTube
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--video_list_path', default = 'video_list.txt')
parser.add_argument('--video_path', default='./data/video')

args = parser.parse_args()



# video list to extract
video_list = open(args.video_list_path,'r')

while True:
    line = video_list.readline()
    if not line: break

    ## youtube homepage link
    yt = YouTube(line)
    yt.streams.filter(progressive=True, 
        file_extension= 'mp4').order_by('resolution').desc().first().download(args.video_path)

    print('[Video Downloaded] {}'.format(line))

video_list.close()