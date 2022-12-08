import os
from moviepy.editor import *
from pytube import Playlist
playlist = Playlist(
    "https://youtube.com/playlist?list=PLdUtBNgqNWqlMn_EUMJpEpL8qNBN5v3UD")
count = 0
for video in playlist.videos:
    video.streams.get_highest_resolution().download()
    count += 1
    print("Downloaded", count, "videos")
print("Downloaded all videos")
