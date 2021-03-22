## python -m pip install pytube

from pytube import YouTube

## youtube homepage link
yt = YouTube('https://www.youtube.com/watch?v=PE7ut70U1_A')
yt.streams.filter(progressive=True, 
    file_extension= 'mp4').order_by('resolution').desc().first().download('./data/video')