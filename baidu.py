#!/usr/bin/env python
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import urllib2
import time
import sys

#youdao_url = 'http://mp3.baidu.com/m?f=ms&rf=idx&tn=baidump3&ct=134217728&lf=&rn=&word=%C0%CF%C4%D0%BA%A2+%BF%EA%D7%D3%D0%D6%B5%DC&lm=-1'
song_name = sys.argv[1]
song_url_name = urllib.quote(song_name.decode(sys.stdin.encoding).encode('gbk'));
youdao_url = 'http://mp3.baidu.com/m?word=' + song_url_name + '&lm=-1&f=ms&tn=baidump3&ct=134217728&lf=&rn='
print youdao_url
d = pq(url=youdao_url)
try:
    p = d("div#tingResults td.down:first a.btn_replace")
    ting_url = p.attr('href')
    print ting_url
    p = d("div#tingResults td.eighth:first span")
    tmp = p.text()
    print tmp
    song_type = tmp[0:3]
    print song_type
    d = pq(url=ting_url)    
    p = d("div.operation a.btn-download")
    song_url = 'http://ting.baidu.com' + p.attr('href').encode("utf-8","ingnore")
    print song_url
except Exception, e:
    print e
    try:
        p = d('div#songResults td.down a.btn_replace:first')
        ting_url = p.attr('href').encode("utf-8",'ingnore')
        print ting_url
        d = pq(url=ting_url)
        p = d("div#main form#form-download div.format b")
        tmp = p.text()
        print tmp
        song_type = tmp[0:3]
        print song_type
        p = d("a#downlink")
        song_url = 'http://mp3.baidu.com' + p.attr('href').encode("utf-8","ingnore")
        print song_url
    except Exception, e:
        print e
        print 'some error happen'
        sys.exit()

print song_url
req = urllib2.Request(url=song_url)
f= urllib2.urlopen(req)
fp = open(song_name.decode(sys.stdin.encoding).encode(sys.stdin.encoding) + '.' +song_type.lower(), 'wb')
song_data = f.read()
fp.write(song_data)
#song_data = f.read(1024)
#while len(song_data): 
#    time.sleep(1)
#    fp.write(song_data)
#    song_data = f.read(1024)
fp.close()
