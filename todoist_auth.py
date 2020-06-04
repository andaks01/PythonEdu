import requests
import json

token = "c11356b85829c502b3b3dd191859982a52c629fb"
all_projects = requests.get("https://api.todoist.com/rest/v1/projects/2226941413", headers={"Authorization": "Bearer %s" % token, 'Content-Type': 'application/json'}).json()
#print(json.dumps(all_projects[1], sort_keys=True, indent=4))
print(json.dumps(all_projects, sort_keys=True, indent=4))

### next commit