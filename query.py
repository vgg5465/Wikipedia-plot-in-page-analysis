import requests

def query(titolo):
  #Function that create the link for the query and return the json
  titolo_replaced = titolo.replace(" ","%20")
  
  #Base link created with wp special page: https://it.wikipedia.org/wiki/Speciale:ApiSandbox
  url = 'https://it.wikipedia.org/w/api.php?action=parse&format=json&page='+titolo_replaced+'&prop=wikitext&section=1&disabletoc=1&formatversion=2'
  
  headers = {
    'Authorization': ' /* PASTE YOUR KEY HERE *\ ',
    'User-Agent': 'plot lenght check'
  }
  
  response = requests.get(url, headers=headers)
  data_json = response.json()
  return(data_json)
