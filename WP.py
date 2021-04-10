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

class code():
	ok = "[\033[92m+\033[0m]"
	info = "[\033[94m*\033[0m]"
	error = "[\033[31m-\033[0m]"
	critical = "[\033[41m!\033[0m]"

def banner():
	print("\n\033[1mWPUserEnum by t0rt3ll1n0, v. 1.4 - don't use for illegal purposes!!\033[0m\n")

def main(url, code):
	if url.endswith("/"):
		url = url[:-1]
	wp_path = "/wp-json/wp/v2/users"
	final = url + wp_path
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
	req = requests.get(final, headers=headers)
	if req.status_code == 200:
		pass
		try:    
			raw_json = req.text
			raw_text = json.loads(raw_json)
		except ValueError:
			#json.decoder.JSONDecodeError:
			print(f"{code.error} An error occurred while loading json, maybe the site redirect to another page. Check manually")
			exit(0)
		slug = "slug"
		total = 0
		for slug in raw_text:
			total += 1
		print(f"{code.ok} {str(total)} Users found\n")
		for x in range(0, len(raw_text)):
			user_id = raw_text[x]['id']
			full_name = raw_text[x]['name']
			user_name = raw_text[x]['slug']
			print(f"User ID: {str(user_id)}")
			print(f"Name: {str(full_name)}")
			print(f"Username: {str(user_name)}")
			line_leght = 10 + len(user_name)
			print("-"*int(line_leght))

	elif req.status_code == 401:
		print(f"\n{code.error} Got 401 unauthorized")
		exit(0)
	elif req.status_code == 403:
		print(f"\n{code.error} Got 403 forbidden")
		exit(0)
	elif req.status_code == 404:
		print(f"\n{code.error} Got 404 not found")
		exit(0)
	elif req.status_code == 500:
		print(f"\n{code.error} Got 500 internal server error")
		exit(0)
	else:
		print(f"\n{code.error} Got an unknown status code: {str(req.status_code)}")

try:
	banner()
	main(url, code)
except Exception as error:
	print(f"\n{code.critical} An error occurred: {error}\n")
