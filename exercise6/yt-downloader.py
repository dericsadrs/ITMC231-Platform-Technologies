# Filename:
#      yt-downloader.py
#
# Descrition:
#      implements a multithreaded program which will take 
#      urls from links.txt and download and convert them to mp3 concurrently  
#
# Author:
#     San Andres Deric  C
#      dsanandres@gbox.adnu.edu.ph
#      Ateneo de Naga University
#
# Course and Year: 
#	BS IT - 2 
#
# Honor code: 
# 	  I have not given nor received any unathorized help in completing this exercise. 
#	  #I am also well aware of the stipulated policies in the AdNU student handbook.
#
#  

from __future__ import unicode_literals
from datetime import datetime
import youtube_dl
from threading import *

# Timestamp: Start Download
print("Time started :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def download(download_link):

    youtbubeURL = []
    youtbubeURL.append(download_link) 
    
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
    ydl.download(youtbubeURL)
    
 
if __name__ == "__main__":

    # Read contents of file 'links.txt'
    url_file = open("links.txt", "r")
    urls = url_file.readlines()

    #store all the threads in a list
    threads = [] 
    
    # creates a thread for every youtube link in the urls list
    for youtubeLinks in urls: 
        thread = Thread(target=download, args=(youtubeLinks,)) 
        threads.append(thread) 

    # starts the download
    threads[0].start() 
    threads[1].start() 

    #join
    threads[0].join()
    threads[1].join()

    # Timestamp: End Download
    print("Time ended :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
