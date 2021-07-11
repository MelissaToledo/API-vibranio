import requests

# Para construccion
"""
data = {
    "nombre producto": "xxx",
    "tipo": "xxx",
    "descripcion": "xxx",
    "precio": 100,
    "tienda": "xxx",
    "link": "xxx.com",


}

response = requests.get("http://127.0.0.1:5000/construccion/1")
response = requests.post("http://localhost:5000/construccion/1")

messageJson = response.json()
print(messageJson)
"""

# Para electricidad
"""
data = {
    "nombre producto": "xxx",
    "tipo": "xxx",
    "descripcion": "xxx",
    "precio": 100,
    "tienda": "xxx",
    "link": "xxx.com",
}

"""
response = requests.get("http://127.0.0.1:5000/electricidad/1")
# response = requests.post("http://localhost:5000/electricidad/1")

messageJson = response.json()
print(messageJson)


# Para poda de arboles
"""
data = {
    "nombre producto": "xxx",
    "tipo": "xxx",
    "descripcion": "xxx",
    "precio": 100,
    "tienda": "xxx",
    "link": "xxx.com",


}

response = requests.get("http://127.0.0.1:5000/poda/1")
response = requests.post("http://localhost:5000/poda/1")

messageJson = response.json()
print(messageJson)

"""
