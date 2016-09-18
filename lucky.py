#! /usr/bin/python3
# This script opens several Google search results

import requests, sys, webbrowser, bs4

#Read the command line args
if len(sys.argv) > 1:
	print('Googling...') 						#display text while downloading the google page
	res= requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
	res.raise_for_status()

	# Now retrieve top search result links
	soup= bs4.BeautifulSoup(res.text, "lxml")
	linkElems= soup.select('.r a')

	#Open a browser tab for each result
	numOpen = min(5, len(linkElems))

	for i in range(numOpen):
		webbrowser.open('http://google.com' + linkElems[i].get('href'))	



