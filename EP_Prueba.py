import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

if response.status_code == 200:
    print("La solicitud fue exitosa, el código de estado es :", response.status_code)
    
    body = json.loads(response.content)
    print("El body de la respuesta es:\n ", body)

else:
    print("La solictud falló, código de estado:", response.status_code)
