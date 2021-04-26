## python -m pip install pytube

from pytube import YouTube

# video list to extract
video_list = open('video_list.txt','r')

while True:
    line = video_list.readline()
    if not line: break

    ## youtube homepage link
    yt = YouTube(line)
    yt.streams.filter(progressive=True, 
        file_extension= 'mp4').order_by('resolution').desc().first().download('./data/video')

    print('Audio Extracted: {}'.format(line))

video_list.close()