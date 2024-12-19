
import csv
import json

# Read the TSV file
with open('/c:/_git/Python/source/asa-saj-a.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    rows = list(reader)

# Create JSON bodies for each row
json_bodies = []
for row in rows:
    json_body = {
        "Environment": row["Environment"],
        "PrincipalName": row["PrincipalName"],
        "PrincipalType": row["PrincipalType"],
        "PrincipalRole": row["PrincipalRole"],
    }
    json_bodies.append(json_body)

# Print JSON bodies
for json_body in json_bodies:
    print(json.dumps(json_body, indent=4))