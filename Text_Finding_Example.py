# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:38:54 2018

@author: peter
"""

# Peter Caya
# 2/3/2018
# The purpose of this script is to accomplish the following:
#   [1]  Download a text from the Project Gutenburg library.
#   [2]  Load the text as a string for python.
#   [3]  Save the text to "Resources" folder.
#   [4]  Break the string into sentences.
#   [5]  Look for instances of <<il y a>> in each sentence.

%reset
# Preamble:
import nltk as nltk
import urllib as urllib
import os
os.chdir("C:/Users/peter/OneDrive/Documents/Learning Stuff/NLP")
#   [1]  /  [2]
text_url = "http://www.gutenberg.org/files/42131/42131-0.txt"
gutenburg_text = urllib.request.urlopen(text_url).read().decode("utf-8")

#   [3]
if os.path.exists("Resources/")==False:
    os.mkdir("Resources")
write_gutenburg = open(file = "Resources/Test_Files.txt",mode = "w+",encoding = 'utf-8')
write_gutenburg.write(gutenburg_text)
write_gutenburg.close()

# [4] 
# Taken from https://stackoverflow.com/questions/4576077/python-split-text-on-sentences

# -*- coding: utf-8 -*-
import re
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

split_text = split_into_sentences(gutenburg_text)


# [5] 

def split_text_find(split_text,ret_string):
    string_placement_vector = list()    
    for i in range(0,len(split_text)-1):
        cur_string = split_text[i]
        string_placement = cur_string.find(ret_string)
        if string_placement != -1:
            string_placement_vector.append(cur_string)
    return(string_placement_vector)
        

search_indices = split_text_find(split_text=split_text,ret_string="il y a")



