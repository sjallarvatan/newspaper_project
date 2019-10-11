import io
import sys 
import os
import pandas as pd 

#uses text list generated with detect_text_google.py inconjunction with a text file containing a commar separated list to pull out all image file names containing those words.#

text_list = sys.argv[1]
word_list = sys.argv[2]

open("image_list.txt", "a+")

def word_lookup(picture_text, words):
	includes = []
	for word in words:
		location = picture_text.find(word.strip())
		if location is not -1:
			includes.append(word.strip())
	if includes:
		print(str(text_table.iloc[index]['image_file']), end=" ", file=photos_search)
		print(includes, end="\n", file=photos_search)	    

photos_search = open("photos_search.txt", "a+")

with open(text_list) as text_list:
    text_table = pd.read_csv(text_list, header=None, names = ["image_file", "text"], sep= "\|\|\|", engine='python')
    word_list_open = open(word_list, "r").read()
    for index, row in text_table.iterrows():
        #print(str(text_table.iloc[index]['image_file']), end="")
        word_lookup(str((text_table.iloc[index]['text'])), word_list_open.split(","))

