import sys
import re
import logging
import json
import requests
from bs4 import BeautifulSoup as bs

logging.basicConfig(level=logging.DEBUG)

url = f"https://catalog.ucdavis.edu/courses-subject-code/ecs/"

response = requests.get(url)
if response.status_code != 200:
	print(response)
	sys.exit(1)

soup = bs(response.content, "html.parser")

# Get all subject codes
subject_ul = soup.find("ul", {"id": "/courses-subject-code/"})
subject_list = subject_ul.find_all("li")

# define regular expression pattern to match the name and code
pattern = r'^(.*)\s+\((\w+)\)$'

subjects = []
# Iterate through subjects
for subject in subject_list:
	temp = {}
	name = subject.find("a").text.strip()

	# use regex to extract the name and code
	match = re.match(pattern, name)
	if match:
		# extract name and code
		name = match.group(1)
		code = match.group(2)

		temp["name"] = name
		temp["code"] = code

	subjects.append(temp)

# Covert courses to JSON object
json_data = json.dumps(subjects)
print(json_data)