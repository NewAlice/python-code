#!/usr/bin/python  
import re   
import urllib  
def getHtml(url):  
    page=urllib.urlopen(url)  
    html=page.read()  
    return html  
def getMp4(html):  
    #r=r"href='(http.*\.h)'"
    r=r'href="(.+?)"'
    re_mp4=re.compile(r)  
    mp4List=re.findall(re_mp4,html)  
    filename=1  
    for mp4url in mp4List:
        print mp4url
        mpurl="https://stuff.mit.edu/afs/sipb/project/merakidev/include/linux/"+mp4url
        try:
            urllib.urlretrieve(mpurl,"%s.h" %mp4url)
            print  'file "%s.h" done' %mp4url  
            filename+=1 
        except Exception as e:
             pass   
 
#url=raw_input("please input the source url:")
url="https://stuff.mit.edu/afs/sipb/project/merakidev/include/linux/"  
html=getHtml(url)  
getMp4(html)  