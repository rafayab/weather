import requests
import json


def prediccion(municipio):
    querystring = {'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJyYWZhLnlhbmV6QHByb3Rvbm1haWwuY29tIiwianRpIjoiNmM3NThlMjctNWI0Ni00OWQ0LWFmNTctNGYwYzQ1MTk3ZDQzIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2Mzg3MzIzNjAsInVzZXJJZCI6IjZjNzU4ZTI3LTViNDYtNDlkNC1hZjU3LTRmMGM0NTE5N2Q0MyIsInJvbGUiOiIifQ.e10wcGIa1cLtOLBOdtMax1ucXSTLI8cWbq3dtEYn2xA'}
    url = 'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/' + municipio

    headers = {
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    resp_json = json.loads(response.text)
    url_data = resp_json['datos']
    forecast_data = requests.request("GET", url_data, headers=headers)

    return json.loads(forecast_data.text)

def pinta(datos_json):
    print(datos_json['temperatura'])

datos = prediccion('08056')
pinta(datos)
#print(datos)
