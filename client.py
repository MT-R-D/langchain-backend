import requests

inputs = {"input": {"input": "what does eugene think of cats?"}}
response = requests.post("http://localhost:8000/invoke", json=inputs)

res = response.json()
print(res)