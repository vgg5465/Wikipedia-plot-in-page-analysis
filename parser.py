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
  
  #Use the json file created with PetScan (https://petscan.wmflabs.org/) for all the pages to check
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
    
    #extract on a .csv file product title and number of words of the plot
    with open('prove_personali/tabella_finale.csv', 'w') as t:
      t.write(tabella)

 

def parse_page(titolo):
  #function for parse the plot
	
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
