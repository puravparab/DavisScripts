import sys
import logging
import json
import requests
from bs4 import BeautifulSoup as bs

logging.basicConfig(level=logging.DEBUG)

# Get URL from command line	
if len(sys.argv) != 2:
	print("Usage: python course_scraper.py <url>")
	sys.exit(1)
subject_code = sys.argv[1]

url = f"https://catalog.ucdavis.edu/courses-subject-code/{subject_code}/"

response = requests.get(url)
if response.status_code != 200:
	print(response)
	sys.exit(1)

soup = bs(response.content, "html.parser")

# Find all courses
courses_list = soup.find_all("div", class_="courseblock")

courses = []
# Iterate through course list
for course in courses_list:
	temp = {}

	# Get course code
	temp["code"] = course.find("span", class_="detail-code").text.strip()
	# Get course name
	temp["name"] = course.find("span", class_="detail-title").text.strip()
	# Get course credits
	temp["credits"] = course.find("span", class_="detail-hours_html").text.strip()

	# Get description
	temp["description"] = course.find("p", class_="courseblockextra noindent").text.strip()

	# Get prereqs
	try: temp["prerequisites"] = course.find("p", class_="detail-prerequisite").text.strip()
	except: temp["prerequisites"] = ""

	courses.append(temp)

# Covert courses to JSON object
json_data = json.dumps({f"{subject_code}" : courses})
print(json_data)