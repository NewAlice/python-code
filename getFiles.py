import requests
import re
import os
basicUrl='https://stuff.mit.edu/afs/sipb/project/merakidev/include/linux/'

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

html = getHTMLText(basicUrl)
r= re.compile(r'\w*.h')
for filename in r.findall(html):
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            file=requests.get(basicUrl+filename)
            f.write(file.content)