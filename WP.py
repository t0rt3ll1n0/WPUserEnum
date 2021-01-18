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
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
	req = requests.get(final, headers=headers)
	if req.status_code == 200:
		print("\nIt seems like that " + url + " is vulnerable to WordPress User Enum")
		print("\nurl: " + final)
		print("Do you want to enumerate and extract wordpress usernames from " + final + " ? [Y]es / [N]o")
		scelta = input(">>> ")
		if scelta == "Y" or scelta == "y":
			try:    
				raw_json = req.text
				raw_text = json.loads(raw_json)
			except ValueError:
				#json.decoder.JSONDecodeError:
				print("An error occurred while reading json, maybe the site redirect to another page. Check manually")
				exit(0)
			slug = "slug"
			total = 0
			for slug in raw_text:
				total += 1
			print(str(total) + " Users found\n")
			for x in range(0, len(raw_text)):
				user_id = raw_text[x]['id']
				full_name = raw_text[x]['name']
				user_name = raw_text[x]['slug']
				print("User ID: " + str(user_id))
				print("Name: " + str(full_name))
				print("Username: " + str(user_name))
				line_leght = 10 + len(user_name)
				print("-"*int(line_leght))

		elif scelta == "N" or scelta == "n":
			print("Ok, bye...")
			exit(0)
		else:
			print("WTF?")
			exit(0)

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
	print("\nWPUserEnum v1.3 - A basic python script to detect possible wp user enum")
	print("by t0rt3ll1n0, obviously ;)") #WTF
	MakeRequests(url)
except KeyboardInterrupt:
	print("\nCTRL + C detected, aborting...")
