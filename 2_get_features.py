from dotenv import load_dotenv
import os
import csv

load_dotenv()
words_path = os.getenv("WORDS_PATH")
features_path = os.getenv("FEATURES_PATH")

def count_vowels_consonants(lemma):
    vowels = ["a", "e", "i", "o", "u", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Ä", "Ö", "Ü"]
    count_vow = [x for x in lemma if x in vowels]
    count_vow = len(count_vow)
    count_con = len(lemma) - count_vow
    return count_vow, count_con

with open(words_path, mode='r', newline='', encoding='latin-1') as infile, \
     open(features_path, mode='w', newline='', encoding='latin-1') as outfile:    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    #add header:
    header = ["lemma", "gender", "hyphen", "length", "first", "first_two", "first_three", "last", "last_two", "last_three", "last_four", "vowels", "consonants", "vc_ratio"]
    writer.writerow(header)
    for row in reader:
        lemma, gender = row
        #features:
        hyphen = False
        if "-" in lemma:
            hyphen = True
        length = len(lemma)
        first = lemma[0]
        first_two = lemma[0:2]
        first_three = lemma[0:3]
        last = lemma[-1]
        last_two = lemma[-2:]
        last_three = lemma[-3:]
        last_four = lemma[-4:]
        vowels, consonants = count_vowels_consonants(lemma)
        vc_ratio = 0
        if consonants == 0:
            vc_ratio = vowels
        else:
            vc_ratio = round(vowels/consonants, 2)
        row_items = [lemma, gender, str(hyphen), str(length), first, first_two, first_three, last, last_two, last_three, last_four, str(vowels), str(consonants), str(vc_ratio)]
        writer.writerow(row_items)  #passing strings would split it after every char!
            
