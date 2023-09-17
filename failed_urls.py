import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd



def generatefile(URL,class_id):

    req=requests.get(URL)
    soup=BeautifulSoup(req.content,"html.parser")
    body_content=soup.find_all('div',class_=class_id)
    ptags=body_content[0].find_all('p')
    list_paragraphs=[]
    for p in np.arange(0,len(ptags)):
        para=ptags[p].get_text()
        list_paragraphs.append(para)
    article=" ".join(list_paragraphs)
    return article

url_df=pd.read_excel('Input.xlsx')

#these are the failed idices which have differnt class id or unable to track class id
# I type them maually from terminal 
failed_index=[2,8,17,24,31,37,71,72,80,87,88,92]

# These are different class id that can be tracked by our program ,again i manually go to website and find these class ids
class_ids=['td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',

           #the following id is error page it doesn't contain any data 
           'tdm_block td_block_wrap tdm_block_column_title tdi_116 tdm-content-horiz-center td-pb-border-top td_block_template_1',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'tdm_block td_block_wrap tdm_block_inline_text tdi_118 td-pb-border-top td_block_template_1',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type',
           'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type']


join={key:value for key,value in zip(failed_index,class_ids)}

#generating the text files making sure that file generated sucussefully or not by printing Done with file generation
for i,cls_id in join.items():
    with open(str(f"textfiles/{url_df.URL_ID[i]}.txt"),'w',encoding='utf-8') as f:
        content=generatefile(url_df.URL[i],cls_id)
        f.write(content)
        print(f"{i} : Done")

