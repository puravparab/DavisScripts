import sys
import json
import subprocess

# Get subject codes from subject_codes.json
try:
	with open('subject_codes.json', 'r') as f:
		subject_codes = json.load(f)
except Exception as e:
	print(str(e))
	sys.exit(1)

all_subjects = []
# Iterate over each subject
for subject in subject_codes:
	code = subject["code"]

	# Call course_download.py
	cmd = f'python course_download.py {code}'
	result = subprocess.run(cmd.split(), capture_output=True, text=True)

	courses = json.loads(result.stdout)
	all_subjects.append(courses)

	# Print status of subprocess call
	if result.returncode == 0:
		print(f"Successfully processed subject {code}")
	else:
		print(f"Error processing subject {code}")

# Write all_courses list to JSON file
with open('course_data.json', 'w') as f:
		json.dump(all_subjects, f)