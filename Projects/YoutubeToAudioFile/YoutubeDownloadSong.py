import os
from moviepy.editor import *
from pytube import Playlist
url = input("Enter the Url: ")
playlist = Playlist(url)
count = 0
for video in playlist.videos:
    count += 1
    name = video.title.split(" ")[0]
    video.streams.filter().first().download(
        output_path="Downloads3", filename=name+".mp4")
    clip = AudioFileClip("Downloads/" + name + ".mp4")
    clip.write_audiofile("Downloads/" + name + ".mp3")
    os.remove("Downloads/" + name + ".mp4")
    print("Downloaded " + str(count) + " videos")

for file in os.listdir("Downloads"):
    if file.endswith(".mp4"):
        clip = AudioFileClip("Downloads/" + file)
        clip.write_audiofile("Downloads/" + file[:-4] + ".mp3")
        print("Converted " + file)

# for file in os.listdir("Downloads"):
#     if file.endswith(".mp3"):
#         os.rename("Downloads/" + file, "Downloads2/" + file)
#         print("Moved " + file)

# # Delete all the files from Downloads folder
# for file in os.listdir("Downloads"):
#     if file.endswith(".mp3"):
#         os.remove("Downloads/" + file)
#         print("Deleted " + file)
