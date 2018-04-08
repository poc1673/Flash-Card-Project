# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:50:10 2018

@author: peter
"""

# Purposes of this script:
# Compile text data for verb conjugations.
#  Steps:
#   1.  Get a list of verbs.
#   2.  Take each verb and get the conjugation information for it.
#   3.  Tag each verb as being related to the stem.


# 1.  Get the webpage and save it to the "verb" directory:
#       a.  Load in verb-list.
#       b.  Define function which downloads webpage for verb.

import os
import pandas as pd
import urllib as urllib
import string
os.chdir("C\\Users\\peter\\OneDrive\\Documents\\Learning Stuff\\NLP\\Verb_Data\\")

verb_list = pd.read_csv( "C:\\Users\\peter\\OneDrive\\Documents\\Learning Stuff\\NLP\\Verb_Data\\vebs_for_download.csv.txt"  )

# b.  

def load_page(verb,directory):
    base_url = "http://la-conjugaison.nouvelobs.com/du/verbe/"+verb+".php"
    response = urllib.request.urlopen(base_url )
    webContent = response.read()
    return(str(webContent))
    
hold = load_page("pouvoir","")


def ret_pos(main_string,substring):
        word_indexes = [s.start() for s in re.finditer(substring,main_string)]
        
        return(  )


pouvoir_test = open("test.txt", mode= "w")
pouvoir_test.write(hold)
pouvoir_test.close()



je_index = ret_pos(hold,"je")




test1 = re.compile("je .*\<br \/\>tu")
locs = test1.search(hold)
locs.group(0)








