#! /usr/bin/python3
# This script downloads every single XKCD comic

import requests, os, bs4

url= 'http://xkcd.com'	#starting url
os.makedirs('xkcd', exist_ok= True) 	# store comics in ./xkcd
# os.makedirs() ensures that this folder exists, and exist_ok= True prevents the function from throwing 
# an exception if it already exists

while not url.endswith('#'):			#while there are more pages
	#Download the page
	print('Downloading the page %s...' %url) # print the URL which is being downloaded
	res= requests.get(url)					# res stores the entire html page
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "lxml")

	#find the comic image
	comicElem= soup.select('#comic img')
	if comicElem == []:						# there might not be an image element at times
		print('Could not find comic image.')
	else:
		try:
			comicUrl= 'http:' + comicElem[0].get('src')

			#download the image
			print('Downloading image %s...' %(comicUrl))
			res= requests.get(comicUrl)    # res stores the image file
			res.raise_for_status()

		except requests.exceptions.MissingSchema:	# if raise_for_status fails, handle the exception 	
			#skip this comic
			prevLink = soup.select('a[rel= "prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue

	#save the image to ./xkcd in the current directory
	imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # os.path.basename() will return just the last part of the URL
	
	for chunk in res.iter_content(100000):
		imagefile.write(chunk)

	imagefile.close()

	#get the prev's button url
	prevLink= soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
