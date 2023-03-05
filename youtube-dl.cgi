#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
# import cgitb
# cgitb.enable()
#import youtube_dl
# import sys
from cgi import FieldStorage
from json import dumps
import yt_dlp

# print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: application/json;charset=utf-8")
print()


# id = "fJ9rUzIMcZQ"
form = FieldStorage()
id = form.getvalue('id') 

youtube_dl_properties = { 'quiet' : True, 'cachedir' : '/tmp/' }
with yt_dlp.YoutubeDL(youtube_dl_properties) as ydl:
                yt_url = 'http://www.youtube.com/watch?v='+id
                info = ydl.extract_info(yt_url, download=False)


print(dumps(info))
