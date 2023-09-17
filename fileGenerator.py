from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests



def generateTextFiles(URL, path,i):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    
    # Find the div element with the specified class names which holds the content of article
    body = soup.find('div', class_='td-post-content tagdiv-type' or 'tdb-block-inner td-fix-index')
    
    if body:

        #finding the p tags and li tags
        x_p = body.find_all('p')
        x_li = body.find_all('li')
        x = x_p + x_li
        
        list_paragraphs = []
        #iterating over th tags get the individual content from each tag and dumping into a list(list_paragraphs)
        for p in np.arange(0, len(x)):
            para = x[p].get_text()
            list_paragraphs.append(para)
        
        #joining the list items into a single article(string)
        final_article = "".join(list_paragraphs)
        
        #Generating the new text file and dumping the finala_article into the file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(final_article)
    else:
        #if unable to write into file because of unmatched classid,
        #  then printing the idexes of datafrme so that again we can do some operation on those files
        print("Required content not found on the page.", "index : ",i)



url_df=pd.read_excel('Input.xlsx')


#str(f"textfiles/{url_df.URL_ID[i]}.txt") gives a file path from URLID to generate textfiles with URL ID as name using generateTextFiles
for i in range(len(url_df)):
    generateTextFiles(url_df.URL[i],str(f"textfiles/{url_df.URL_ID[i]}.txt"),i)



