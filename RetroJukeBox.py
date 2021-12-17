from typing import Text
import requests
from bs4 import BeautifulSoup
import os
Foldername = input('This is the album title: ')
File = os.mkdir(Foldername)
Curr_Directory = os.getcwd()+'/'+ Foldername
os.chdir(Curr_Directory)
print(Curr_Directory)
#This is supoosed to be the url given from the user 
url = str(input('Please Enter In A Valid Khinsider Album Url: ')).replace(' ','')
#This is supposed to be the new folder

req = requests.get(url.format(1))
Base_Url='https://downloads.khinsider.com'
def dLink(Url, Name):
    """[summary]
    This was shamelessly borrowed from a yoyutbe video about donwlaoding fiels using python
    Args:
        Url (User String input, has to validated beforehand): [description]
        Name (key)): [suppsoed to be used alongside the 'Urls' dictionary, The keys are the file names]
    """
    req = requests.get(Url)
    with open(Name,'wb') as file:
        for chunk in req.iter_content(chunk_size=1000):
            if chunk:
                file.write(chunk)
#^^^^^^^^^^^^^^^^^^^This is the download function
#with open(lol,'r') as r:
soup = BeautifulSoup(req.text, 'lxml')
#print(soup)
# NOW AFTER A WHOLE WEEK FINALLY, This Url will store each link to the download page
Lame_Counter =0
Limit = 3
#Got to make this since I can't find just one tage with just ONE ELEMENT just stupid man
Urls={}
for td in soup.find_all('td', class_="clickable-row"):
    #Ok this kinda means at least to my small brain, that beautiful soup parse throguh the html and stores each eleemnt and attribute as a dict I think I'm not too sure
    
    if Lame_Counter < 1:
        Urls[td.getText()] = td.find("a")['href']
    Lame_Counter +=1
    if Lame_Counter == 3:
        Lame_Counter = 0
#Ok the use of "Lame Counter" was becasue of my lack of knwoledge ofn the subejct of ebautiful soup, it became frustring so i went tow at I knew, and I used a coutner to 
# count the elements I wanted to get, I tested it out on multiple urls to ensure that this wasn't a fluke
Page2 = []
Titles = []
#This list holds all the songnames and stuff assocaited with the uh album link provided
#Now this contains every single download page link jeez this took too long
for SongName in Urls:
    Page2.append(Base_Url+ Urls[SongName])
    Titles.append(SongName)

Tracklist = {}
for songs in range(len(Page2)):
    Tracklist[Titles[songs]] =Page2[songs]
#tHIS IS A DICT OF ALL THE FINAL URLS AND THE UH LINKS ASSCOIATED WITH THEM
for Track in Tracklist:
    req2 = requests.get(Tracklist[Track].format(1))
    sort = BeautifulSoup(req2.text, 'lxml').find('audio')['src']
    dLink(sort,Track+'.mp3')
