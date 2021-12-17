# Retro-Jukebox
A simple Music Downloader for Kinder
UPDATE LOG, THIS IS NOT DONE YET, I'll delete the extra files when it's done, BIGGEST ISSUE IS PARSING THRU AND FINDING OUT WHERE TO FIND SONG TITLES
|NOTE|
You need requests in order to make this script work, this was also done using python, so ensure that you have that installed too
To install requests, all you need to do is open cod or terminal and put in the following command:
"Pip install requests"
"Python -m pip install requests
You May also need to install Beautiful Soup 4 as well, using a similar command as well, I'll link the documentation below

|Brief Background|
This is essentially just a web scraper built to download files one by one from the Insider website. The goal of this project was to successfully bypass their paywall behind downloading videogame soundtracks, as their main gimmick behind running their site is donating to them to mass download whole albums. While I don't know too much about who owns the licensing on the website, it is true that anyone can download each song individually for free without paying them a dime. 
The requests module used within this project is sued in order to send "GET" requests to both download each file and to parse the urn that the user provides.

|References|
Raw String to HTML
https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
"""
Import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext
"""
|Update Log|
This can be used to get the song names
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...
Priority goal, Make sure you can get the text from two speciifc tags with specified classes/ ID's
New Goal Trail/ Follow up on two urls in succession
Find out how to get to the td elements then find out how to get the name, file size, then the url
This helped out with finding the url
THANK YOU STACK OVERFLOW(Found with the search result of "https://www.google.com/search?q=how+to+sort+nested+elemenets+with+hrefs+in+beautiful+soup&rlz=1C1EJFC_enUS895US895&ei=4lC1Yf-vCr6bptQP0J2E8AY&ved=0ahUKEwj_qLzLjt30AhW-jYkEHdAOAW4Q4dUDCA4&uact=5&oq=how+to+sort+nested+elemenets+with+hrefs+in+beautiful+soup&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAEyBwghEAoQoAEyBwghEAoQoAEyBwghEAoQqwIyBwghEAoQqwI6BwgAEEcQsANKBAhBGABKBAhGGABQhARYyB5g7SBoAXABeACAAbwCiAHhHpIBCDAuNC4xMC4zmAEAoAEByAEIwAEB&sclient=gws-wiz")
https://stackoverflow.com/questions/41908426/extracting-deeply-nested-href-in-python-with-beautiful-soup
ROADBLOCK!
Theres no way to get 1 strict way of urls, howevery, I can do soemthing a little weir
Expeirmenting now, i found that by usign "getText" I can get the text at a certain thingie in time
New code
Page2 = []
Songs = 
#Now this contains every single download page link jeez this took too long

for SongName in Urls:
    Page2.append(Base_Url+ Urls[SongName])
    SongTitles[SongName] 
    req2 = requests.get(Page2[Songs].format(1))
    sort = BeautifulSoup(req2.text, 'lxml').find('audio')['src']
    )
print(sort)
print(req2)
print(Page2)
