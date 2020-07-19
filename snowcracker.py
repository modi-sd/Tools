#!/usr/bin/env python
import os
import sys
if len(sys.argv) != 3:
	print("usage : snowcracker.py wordlist file")
else:
	wordlist = open(sys.argv[1], "r")
	ct = sys.argv[2]
	for password in wordlist:
		stripped_password = ''.join(password.split())
		str = 'stegsnow -C -Q -p \''+stripped_password+'\' '+ct
		print(str+"\n")
		os.system(str)
		print("\n")
