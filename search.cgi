#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from cgi import FieldStorage
from pytube import Search
#from urllib import parse

print("Content-Type: application/json;charset=utf-8")
print()


form = FieldStorage()
id = form.getvalue('id') 

s = Search(id)

print('{ "items" : [')

for v in s.results:
  vidId = v.watch_url.split("=")[1]  #parse.parse_qs(parse.urlparse(v.watch_url).query)['v'][0]
  title = v.title.replace('"', "'")
  print(f' {{ "id" : {{ "videoId" : "{vidId}", "title": "{title}", "url": "{v.watch_url}" }} }}, \n')

print(' { "id" : { } } ]}')

