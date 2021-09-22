#!/usr/bin/env python3

import time
import sys

username = input("Enter your Username:")
password = input("Enter your Password:")
time.sleep(1)
if password == "assbutt123":
	print("\nAccess Granted\n")
	print("\nWelcome!",username.capitalize())
else:
	print("\nAccess Denied")
	sys.exit()

count = "yes"
while count.lower() == "yes":
	
	print("\nThe files you are having are <batman.txt>,<got.txt>...\n")


	filename = input("Enter the name of the file you want to open:")
	try:
		file = open(filename)
	except:
		print("\nFile cannot be opened\n")
		sys.exit()
	
	print("\nAcecessing Files...")

	time.sleep(2)
	char = input("Whose Dialoge do you want to read:")

	print("\nLoading...\n")

	time.sleep(5)

	print("\nReceived Files\n")
	for lines in file:
		line = lines.strip()
		if line.startswith(char):
			print(line)

			
	count = input("\nDo you want to read another file: {enter yes to continue}:")



		
print("\n\nPlease enter exit")
