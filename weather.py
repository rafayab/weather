import requests

key = 'xxx'
url = 'https://api.meteo.cat/referencia/v1/municipis'
 
response = requests.get(url, headers={"Content-Type": "application/json", "X-Api-Key": key})
 
print(response.status_code)  #statusCode
print(response.text) #valors de la resposta
// TODO fer el tractament que es vulgui amb les dades de resposta
 