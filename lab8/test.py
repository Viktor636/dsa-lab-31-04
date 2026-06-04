import requests

BASE = "http://127.0.0.1:5000"

# SET
print(requests.post(f"{BASE}/set", json={"key": "name", "value": "Viktor"}).json())
print(requests.post(f"{BASE}/set", json={"key": "city", "value": "Novosibirsk"}).json())
print(requests.post(f"{BASE}/set", json={"key": "age", "value": "20"}).json())

# GET
print(requests.get(f"{BASE}/get/name").json())
print(requests.get(f"{BASE}/get/city").json())
print(requests.get(f"{BASE}/get/age").json())
print(requests.get(f"{BASE}/get/group").json())

# EXISTS
print(requests.get(f"{BASE}/exists/name").json())
print(requests.get(f"{BASE}/exists/city").json())
print(requests.get(f"{BASE}/exists/age").json())
print(requests.get(f"{BASE}/exists/group").json())

# DELETE
print(requests.delete(f"{BASE}/delete/name").json())
print(requests.get(f"{BASE}/get/name").json())
