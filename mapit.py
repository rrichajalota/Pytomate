#! /usr/bin/python3
# mapIt.py - launches a map in the browser using an
# address from the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	#get address from command line

	address = ' '.join(sys.argv[1:]) 

	#command line args are joined by a space as separator
	#sys.argv[1:] chops off the first element of the array which is the program name

else:
	# get the address from the clipboard
	address = pyperclip.paste()

webbrowser.open(address)

