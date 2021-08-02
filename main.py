#!/usr/bin/python

import requests
import re

regex = r"(\w{32,}?)\s+\d+?\s+(.*)$"


def read_checksums(url):
    req = requests.get(url)
    matches = re.finditer(regex, req.text, re.MULTILINE)
    for matchNum, match in enumerate(matches):
	if(re.search("\\.gz$",match.groups()[1])):
		result="Checksum: "+match.groups()[0]+" \t Filename: "+match.groups()[1]+""
        	print(result)


read_checksums('http://ftp.debian.org/debian/dists/jessie/Release')
