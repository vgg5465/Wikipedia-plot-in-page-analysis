import requests

def query(titolo):
  url = 'https://it.wikipedia.org/w/api.php?action=parse&format=json&page=Avatar%20(film%202009)&prop=wikitext&section=1&disabletoc=1&formatversion=2'

  titolo_replaced = titolo.replace(" ","%20")
  
  url = 'https://it.wikipedia.org/w/api.php?action=parse&format=json&page='+titolo_replaced+'&prop=wikitext&section=1&disabletoc=1&formatversion=2'
  
  headers = {
    'Authorization': 'PASTE YOUR KEY',
    'User-Agent': 'plot lenght check'
  }
  
  response = requests.get(url, headers=headers)
  data_json = response.json()
  return(data_json)