# we used two for cycle to get the data

for tr in soup.findAll('tr'):
    for td in tr.findAll('td'):
        if "http" in (td.text):
            movieslist.append(td.text)
        
for i in range(0,10000):
    time.sleep(3)
    response = urlopen(movieslist[i])
    namefile = "article_" + str(i)+ ".html"
    with open(namefile, "wb") as f:
        f.write(response.read())
        f.close()
