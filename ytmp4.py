# Code contributed by
# Shrimad Bhagwat

from pytube import YouTube
import youtube_dl
from pytube import Playlist

p= Playlist("<Playlist Link (Playlist should be public or unlisted)>") # Music Playlist Link
length = p.length
count = 1
for url1 in p.video_urls:
    url = url1
    print(str(count) + "/" + str(length))
    
    my_video = YouTube(url)

    print("*********************Video Title************************")
    #get Video Title
    print(my_video.title)

    print("********************Tumbnail Image***********************")
    #get Thumbnail Image
    print(my_video.thumbnail_url)

    print("********************Download video*************************")
    #get all the stream resolution for the 
    for stream in my_video.streams:
        print(stream)

    #set stream resolution
    my_video = my_video.streams.get_highest_resolution()

    #or
    #my_video = my_video.streams.first()

    #Download video
    my_video.download()
    count += 1