import requests

kw = {'flag': 1}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get("http://127.0.0.1:8080/MyApp/make_data_for_school_hospital", params = kw, headers = headers)

print(response.text)