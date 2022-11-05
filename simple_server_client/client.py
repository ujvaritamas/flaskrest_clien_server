import requests
api_url = "http://localhost:5001/todo/api/v1.0/tasks"
#test get
response = requests.get(api_url)
print(response.json())