#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
# import cgitb
# cgitb.enable()
import youtube_dl
# import sys
import cgi
import json


# print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: application/json;charset=utf-8")
print()


# id = "fJ9rUzIMcZQ"
form = cgi.FieldStorage()
id = form.getvalue('id') 

youtube_dl_properties = { 'quiet' : True, 'cachedir' : '/tmp/' }
with youtube_dl.YoutubeDL(youtube_dl_properties) as ydl:
                yt_url = 'http://www.youtube.com/watch?v='+id
                info = ydl.extract_info(yt_url, download=False)


print(json.dumps(info))
