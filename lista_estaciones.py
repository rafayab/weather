import requests


url = 'https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/'
 
querystring = {'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJyYWZhLnlhbmV6QHByb3Rvbm1haWwuY29tIiwianRpIjoiNmM3NThlMjctNWI0Ni00OWQ0LWFmNTctNGYwYzQ1MTk3ZDQzIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2Mzg3MzIzNjAsInVzZXJJZCI6IjZjNzU4ZTI3LTViNDYtNDlkNC1hZjU3LTRmMGM0NTE5N2Q0MyIsInJvbGUiOiIifQ.e10wcGIa1cLtOLBOdtMax1ucXSTLI8cWbq3dtEYn2xA'}
headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

