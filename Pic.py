import requests
from time import sleep
with open('00000001.jpg','wb') as f:
	f.write(requests.get('http://www.twitter.com/pmikpti').content)
