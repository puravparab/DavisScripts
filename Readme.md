# Scripts for Davis Course Search
All of the scripts and notebooks I used for Davis COurse Search including a webscraper for getting UC DAvis courses , creating embeddings and uploading them to a pinecone vector db

## Requirements
- `python 3.10`
- OPEN AI Account
- Pinecone Index`

## Installation
Clone repository
```
git clone https://github.com/puravparab/DavisScripts.git
cd DavisScripts
```
Get virtual environment running
```
pip install --user pipenv
pipenv shell
pipenv sync
```
Create .env file and setup environment variables
```
OPENAI=<Your OpenAI secret key>
PINECONE=<Add your Pinecone Index Key>
PINECONE_ENV=<Pinecone environment>
````

## Usage

* #### course_download.py:
	Get all courses of specified subject and store it in data.json
```
python course_download.py <subject code> > data.json
````

* #### get_subject_codes.py:
	Get all subjects and store their codes in subject_codes.json
```
python get_subject_codes.py > subject_codes.json
````

* #### get_all_courses.py:
	Get all courses of all subjects and store them in course_data.json
```
python get_all_courses.py
````

* #### sematic_search.ipynb
	Get embeddings for course_data.json and prompt them

* #### pinecone.ipynb:
	Converting embeddings into json that can be inserted into a pinecone index