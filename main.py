import time

print("Welcome to Ultra YouTube Downloader and Converter v1.0")
time.sleep(1)
print("Loading...")
time.sleep(3)

from pytube import YouTube

link = input("Paste your link here: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()
print("Done!")
