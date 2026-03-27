import requests
import random

BASE_URL = "http://localhost:5000"

# 1. GET 
get_param = random.randint(1, 10)
print(f"GET запрос с param={get_param}")

response_get = requests.get(f"{BASE_URL}/number/", params={'param': get_param})
data_get = response_get.json()
print(f"Ответ GET: {data_get}")

# 2. POST 
post_param = random.randint(1, 10)
print(f"\nPOST запрос с jsonParam={post_param}")

headers = {'Content-Type': 'application/json'}
response_post = requests.post(
    f"{BASE_URL}/number/",
    json={'jsonParam': post_param},
    headers=headers
)
data_post = response_post.json()
print(f"Ответ POST: {data_post}")

# 3. DELETE 
print("\nDELETE запрос")

response_delete = requests.delete(f"{BASE_URL}/number/")
data_delete = response_delete.json()
print(f"Ответ DELETE: {data_delete}")

# 4. Выражение
results = [
    data_get['result'],
    data_post['result'],
    data_delete['result']
]

operations = [
    data_get['operation'],
    data_post['operation'],
    data_delete['operation']
]

print(f"\nПолученные числа: {results}")
print(f"Операции: {operations}")

calc_result = results[0]

ops = {
    'sum': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y
}

for i in range(2):
    calc_result = ops[operations[i]](calc_result, results[i + 1])

final_result = int(calc_result)
print(f"\nРезультат вычислений: {final_result}")

expression = f"{results[0]}"
for i in range(2):
    op_symbol = {'sum': '+', 'sub': '-', 'mul': '*', 'div': '/'}[operations[i]]
    expression += f" {op_symbol} {results[i + 1]}"
expression += f" = {calc_result} ≈ {final_result}"

print(f"\nВыражение: {expression}")