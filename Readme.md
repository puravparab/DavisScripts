# Scripts for Davis Course Search

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

* #### pinecone.py:
	Take generated embeddings in course_embeddings.csv and turn them in json that can be used by pinecone
```
python pinecone.py > pinecone_embeddings.json
````