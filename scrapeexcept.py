from urllib.request import urlopen
from urllib.error import HTTPError

try:
	html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
	print(e)
except URLError as e:
	print("URL Not Found")

	#return null,break,error
else:
	print("It works")