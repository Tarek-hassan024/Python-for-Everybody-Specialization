import urllib
from BeautifulSoup import *

URL = raw_input("Enter the URL:") #Enter main URL
link_line = int(raw_input("Enter position:")) - 1 #The position of link relative to first link
count = int(raw_input("Enter count:")) #The number of times to be repeated

while count >= 0:
    html = urllib.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(URL)
    URL = tags[link_line].get("href", None)
    count = count - 1