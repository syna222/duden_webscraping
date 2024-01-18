from bs4 import BeautifulSoup
import pandas as pd
import requests

csv_path = "wörter_und_genus.csv"
page_numbers = {"ä": 0, "ö": 0, "ü": 0, "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,"i": 0, "j": 0, "k": 0, "l": 0,"m": 0, "n": 0, "o": 0, "p": 0,"q": 0, "r": 0, "s": 0, "t": 0,"u": 0, "v": 0, "w": 0, "x": 0,"y": 0, "z": 0}

def get_pagenumbers():
    for key in page_numbers.keys():
        url = f"https://www.duden.de/suchen/dudenonline/{key}?_wrapper_format=html&page=5000"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        last_page = int(soup.find(title="Aktuelle Seite").text) - 1
        page_numbers[key] = last_page
        
def get_wordlist_typelist(url):  #suchseite
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        words = soup.find_all("strong")
        words = [w.text.replace("\xad", "") for w in words]
        types = soup.find_all("p", class_="vignette__snippet")
        types = [t.text.replace("\n\n\n", "") for t in types]
        return words, types

get_pagenumbers()
print(page_numbers)
        
###
with open(csv_path, 'a', newline='', encoding="utf-8") as file:
    for key in page_numbers:
        print("@ letter", key)
        for page in range(page_numbers[key] + 1):
                url = f"https://www.duden.de/suchen/dudenonline/{key}?_wrapper_format=html&page={page}"
                #visit every page for the letter and get all words + their word type and gender
                words, types = get_wordlist_typelist(url)
                if len(words) != len(types):
                    raise Exception("words and types are not of the same length!")
                    break
                words_types = []
                for i in range(len(words)):
                    if "Substantiv" in types[i]:
                        wort = words[i]
                        genus = types[i].split(",")
                        if len(genus) > 1:
                            genus = genus[1]
                        else:
                            genus = genus[0]
                        if genus == " feminin" or genus == " maskulin" or genus == " Neutrum":  #Filtern von Eigennamen, Druckversionen etc.
                            words_types.append([wort, genus])
                #append to csv:
                for wort, genus in words_types:
                    file.write(wort + "," + genus.strip() + "\n")
file.close()       
        

