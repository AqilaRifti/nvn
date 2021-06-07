
import requests
import re

def getFilename_fromCd(cd):
	"""
	Get filename from content-disposition
	"""
	if not cd:
		return None
	fname = re.findall('filename=(.+)', cd)
	if len(fname) == 0:
		return None
	return fname[0]


url = 'https://i.ytimg.com/an_webp/79Q4yZuFDyk/mqdefault_6s.webp?du=3000&sqp=CMqQ9oUG&rs=AOn4CLDEsSStiGTTIJzzIERUgmJBlNUtsw'
r = requests.get(url, allow_redirects=True)
open("hello.png", 'wb').write(r.content)
print(r.content)