from query import *
import json
from prettytable import PrettyTable

def main(): 
	
  with open('prove_personali/film_full.json', 'r', encoding='utf-8') as f:
    page_ex_dict = json.load(f)	

  titolo_film_list = []
  final_list = []
  
  x = PrettyTable()
  x.field_names = ["Titolo", "Parole in trama"]
  count = 1

  for i in page_ex_dict:
    film_dict = {}
    titolo_film = i["title"].replace("_"," ")
    titolo_film_list.append(titolo_film)
    print(count,"Analizzando", titolo_film)
    film_dict["titolo"] = titolo_film
    film_dict["trama"] = parse_page(titolo_film)
    film_dict["nr. parole"] = len(film_dict["trama"].split())
    count += 1
    final_list.append(film_dict)
    x.add_row([film_dict["titolo"], film_dict["nr. parole"]])
    tabella = x.get_csv_string()
    with open('prove_personali/tabella_finale.csv', 'w') as t:
      t.write(tabella)

  
  
#  for i in final_list:
#    x.add_row([i["titolo"], i["nr. parole"]])

#  tabella = x.get_csv_string()

#  with open('prove_personali/tabella_finale.csv', 'w') as t:
#    t.write(tabella)

def parse_page(titolo):
  film_json = query(titolo)
  trama_parsed = "*Parsing-Error*"
  try:
    trama_stub = film_json["parse"]["wikitext"]
    trama_parsed = trama_stub.split("\n",1)[1]
  except KeyError:  # includes simplejson.decoder.JSONDecodeError
    print('Errore di parsificazione')
  return(trama_parsed)

if __name__ == "__main__":
    main()