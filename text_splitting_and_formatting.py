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


# Preamble:
import nltk as nltk
import urllib as urllib
import os
import re
os.chdir("C:/Users/peter/OneDrive/Documents/Learning Stuff/NLP")


# Dictionary of replacement cases to clean for stemmer:
clean_dict = {"\\.$":"",
              ",":""}

def poc_cleaner(txt,clean_dict):
    cleaned_txt = txt
    for keys in clean_dict:
        cleaned_txt = re.sub(pattern=keys,repl=clean_dict[keys],string=cleaned_txt)
    return(cleaned_txt)


test_sentence = "L'hier soir, je dinais avec mon frere apres j'ai visite la maison proche a lui."
split_text = test_sentence.split(sep = " ")
updated_text = list()
for strings in split_text:
    updated_text.append(poc_cleaner(txt = strings,clean_dict = clean_dict))
    
