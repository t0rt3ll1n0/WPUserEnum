#!/usr/bin/python3
#encoding: UTF-8
#WPUserEnum by t0rt3ll1n0 - a basic script to check wp user enum

import requests
import sys
import json
import re
import os

try:
    url = sys.argv[1]
except IndexError:
    print("usage: python3 WP.py http://www.site.com")
    exit(0)

def MakeRequests(url):
	if url.endswith("/"):
		url = url[:-1]
	wp_path = "/wp-json/wp/v2/users"
	final = url + wp_path
	req = requests.get(final)
	if req.status_code == 200:
		print("\nIt seems like that " + url + " is vulnerable to WordPress User Enum")
		print("\nurl: " + final)
		print("Do you want to enumerate wordpress usernames from " + final + " ? [Y]es / [N]o")
		scelta = input(">>> ")
		if scelta == "Y" or scelta == "y":    
			raw_json = req.text
'''
            #tried that, but didn't work :(

            raw_data = json.loads(raw_json)
            raw_number = re.findall("slug", raw_data)
            user_number = 0
            for i in len(raw_number):
                user_number += 1
            if user_number < 1:
                print("\nNo users was found")
                exit(0)
            print("\nTotal number of users: " + str(user_number))
'''
			raw_text = json.loads(raw_json)
            #i tried something, here u can see that
			#all_slug = re.findall("slug", raw_text)
			#print(str(all_slug)
			##x = re.findall("slug", txt)
			##print(x)
			slug = "slug"
            total = 0
            for slug in raw_text:
            	total += 1
            if total < 1:
            	if os.name == "NT":
            	#i'm not sure about the path, but i don't have windows so if it gives error submit that#
            		print("\nNo users was found, check manually the json file in C:\wp_users.json")
            		f = open("C:\wp_users.json", "w")
            		f.write(raw_json)
            		f.close()
            		exit(0)
            	else:
            		print("\nNo users was found, check manually the json file in /tmp/wp_users.json")
            		f = open("/tmp/wp_users.json", "w")
            		f.write(raw_json)
            		f.close()
            		exit(0)
            print(str(total) + " Users found")

	elif req.status_code == 401:
		print("\nIt seems like that in " + url + " REST API has been disabled")
		exit(0)
	elif req.status_code == 403:
		print("\nThe REST API are unaccessible: status code " + str(req.status_code))
		exit(0)
	elif req.status_code == 404:
		print("\nGot a 404 (not found) status code")
		exit(0)
	elif req.status_code == 500:
		print("\nUh-Oh, got a 500 status code, maybe there is a kind of WAF")
		exit(0)
	else:
		print("\nGot an unknown status code: " + str(req.status_code))

try:
	print("\nWPUserEnum - A basic python script to detect possible wp user enum")
	print("by t0rt3ll1n0, obviously ;)") #WTF
	MakeRequests(url)
except KeyboardInterrupt:
	print("\nCTRL + C detected, aborting...")
