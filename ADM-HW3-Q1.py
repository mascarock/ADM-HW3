### Question 1 
### Parse downloaded pages

from bs4 import BeautifulSoup
import os
import csv

##  read .HTML files
folder_dir = os.listdir('Html-data')
for i in range(1,10000):
    htmlfile=open(r'Html-data/article_'+str(i)+'.html','r',encoding='utf8')
    soup=BeautifulSoup(htmlfile,'html.parser')
    
    #Find Title of movies
    tsv_content=[]
    dict_content={}
    dict_content['title']=soup.select_one('h1',{"class":"firstheading:"}).text 
    
    # Find intro of movies
    
    pr_content = soup.select('p')
    try:
        dict_content['intro']="".join(pr_content[0].text.strip("\n"))
    except:
        dict_content['intro']="NA"
    
    # Find plot of movies
    try:
        dict_content['plot']="".join(pr_content[1].text.strip("\n"))
    except:
        dict_content['plot']="NA"
        
    for data in dict_content:
        tsv_content.append(dict_content[data])
        
    # Find infobox content 
    table_body=soup.find('tbody')
    if table_body!= None:
        allrows = table_body.find_all('tr')
        for rows in allrows:
            if rows.th!= None:
                if rows.th.text == 'Directed by':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Produced by':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Written by':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Starring':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Music by':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Release date':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Running time':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Country':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text == 'Language':
                    tsv_content.append("".join(rows.td.text.strip("\n")))
                elif rows.th.text =='Budget':
                    tsv_content.append("".join(rows.td.text.strip("\n"))) 
                
    # create .TSV file            
    with open('TSV-data/article_'+str(i)+'.tsv', 'wt') as out_file:
        try:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(tsv_content)
        except:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow('This page not found')