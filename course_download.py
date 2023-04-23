import sys
import requests
from bs4 import BeautifulSoup as bs
import json

# Get URL from command line	
if len(sys.argv) != 2:
	print("Usage: python course_scraper.py <url>")
	sys.exit(1)
subject_code = sys.argv[1]

url = url = f"https://catalog.ucdavis.edu/courses-subject-code/{subject_code}/"

response = requests.get(url)
if response.ok != 200:
	print(response)
	sys.exit(1)

soup = bs(response.content, "html.parser")

# Find all courses
courses_list = soup.find_all("div", class_="courseblock")

courses = []
# Iterate through course list
for course in courses_list:
	temp = {}
	temp["description"] = course.find("p", class_="courseblockextra noindent").text.strip()
	courses.append(temp)

# Covert courses to JSON object
json_data = json.dumps({f"{subject_code}" : courses})
print(json_data)