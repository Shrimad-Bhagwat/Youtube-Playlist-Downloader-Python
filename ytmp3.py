# Code Contributed by
# Shrimad Bhagwat

import youtube_dl
from pytube import Playlist

p= Playlist("<Playlist Link (Playlist should be public or unlisted)>") # Music Playlist Link

count=1 # Counter
def download(url):
    try:
        print("\n----------------------------------------------------------------------\n")
        video_url = url
        print("===>  "+str(count)+"/"+str(p.length))
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        print("\n  Video Name ===> "+f"{video_info['title']}"+"<===     \n")
        filename = f"Files\\{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,  # Audio
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
    except:
        print("Error")
for url in p.video_urls:
    download(url)
    count+=1


print("\nCompleted!\n")