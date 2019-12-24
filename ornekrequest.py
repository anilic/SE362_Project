import requests

request = requests.get('http://10.100.8.9:8000/a.html')
data = request.json()
print('Baslik: ' + str(data['menu']['popup']['menuitem'][0]['value']))
print('Baslik: ' + str(data['menu']['popup']['menuitem'][0]['value']))
#'Title' translated to Turkish by Deniz Kiratli
#Added second print line by H. Berfin Polat
