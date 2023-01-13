from __future__ import unicode_literals
from datetime import datetime
import youtube_dl

# Read contents of file 'links.txt'
url_file = open("links.txt", "r")
urls = url_file.readlines()

# Timestamp: Start Download
print("Time started :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# Define YoutubeDL object and download file
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
ydl = youtube_dl.YoutubeDL(ydl_opts)
ydl.download(urls)

# Timestamp: End Download
print("Time ended :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))