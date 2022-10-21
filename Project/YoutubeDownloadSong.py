import os
from pytube import Playlist
playlist = Playlist("https://youtube.com/playlist?list=PLTnH-2qi9M5PvJEvL28xShjWwI-cFjpt4")

count = 0
# Download the playlist in mp3 format
for video in playlist.videos:
    try:
        video.streams.get_audio_only().download(output_path="Downloads")
        print("Downloaded " + str(count))
        count = count + 1
    except:
        pass


print("Downloaded")

