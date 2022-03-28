import urllib.request as ul
from bs4 import BeautifulSoup as soup
from docx import Document

def getInfo():
    url = "https://www.bbc.co.uk/news/business"
    req = ul.Request(url, headers={'User-Agent':'Chrome'})
    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()

    pagesoup = soup(htmldata, "html.parser")
    itemlocator = pagesoup.find('div', {"class":"gel-layout gel-layout--equal"})

    titles = []
    for items in itemlocator.find_all('h3'):
            title = items.text
            titles.append(title)
            #print(title)
    titles.pop(5)

    summaries = []
    for items in itemlocator.find_all('p'):
            summary = items.text
            summaries.append(summary)
            #print(summary)

    images = []
    for items in itemlocator.find_all('img', {"class":"lazyloaded"}):### not exactly working
            image = items.get('src')
            images.append(image)
            #print(image)

    return titles, summaries, images

def createDocument():

    titles, summaries, images = getInfo()
    
    document = Document()

    document.add_heading('BBC Business News Report', 0)

    p = document.add_paragraph('Here`s the ')
    p.add_run('news').bold = True
    p.add_run(' for ')
    p.add_run('today ').italic = True
    
    for title in titles:
        document.add_heading(title, level=1)
        document.add_paragraph(summaries[titles.index(title)], style='Intense Quote')

    #document.add_picture(src)

    document.save('Documents/Projects/Coding Projects/bbcBusinessNewsBOT/newsReport.docx')

createDocument()