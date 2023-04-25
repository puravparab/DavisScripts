import csv
import json

json_data = {
	"vectors": []
}

def create_row_json(row):
	row_json  = {
		"id": f'item_{row[0]}',
		"metadata":{
			"code": row[1],
			"name": row[2],
			"credits": row[3],
			"description": row[4],
			"prerequisites": row[5]
		},
		"values": json.loads(row[7])
	}
	return row_json

# Read from embeddings
with open('course_embeddings.csv', newline='') as f:
	reader = csv.reader(f, delimiter=',')
	# Skip the header row
	next(reader)
	for row in reader:
		row_json = create_row_json(row)
		json_data["vectors"].append(row_json)

print(json.dumps(json_data))