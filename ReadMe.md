# Retro-Jukebox
A simple Music Downloader for Kinder
UPDATE LOG, THIS IS NOT DONE YET, I'll delete the extra files when it's done, BIGGEST ISSUE IS PARSING THRU AND FINDING OUT WHERE TO FIND SONG TITLES
# |NOTE|
You need requests in order to make this script work, this was also done using python, so ensure that you have that installed too
To install requests, all you need to do is open cod or terminal and put in the following command:
"Pip install requests"
"Python -m pip install requests
You May also need to install Beautiful Soup 4 as well, using a similar command as well, I'll link the documentation below

# |Brief Background|
This is essentially just a web scraper built to download files one by one from the KhInsider website. The goal of this project was to successfully bypass the paywall downloading videogame soundtracks as an album, as their main gimmick behind running their site is donating to them to mass download whole albums. While I don't know too much about who owns the licensing on the website, it is true that anyone can download each song individually for free without paying them a dime. 
The requests module used within this project is used in order to send "GET" requests to sort through the pages HTML, find the URL attached to each track's name, and then download each file to parse the urn that the user provides.
# |How To Run|
-Ensure that you have both the BeatifulSoup and the Requests library installed on your machine. This goes without saying, but also make sure you have the Latest Version of Python installed on your machine as well

-Open the 'RetroJukeBox.py' file in your favorite IDE, and run the file!

-There will be a message in the terminal window saying 'Please Enter In A Valid Khinsider Album Url: ', copy and paste a URL from the website, and press enter

-You'll be asked to provide an album name, **this is the name of the Folder that your tracks will be held in**. I'd recommend storing it as the name of the videogame or maybe something unique to prevent any errors 

# |References|
Raw String to HTML
https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
"""
Import re
as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext
"""
Requests
-https://docs.python-requests.org/
Beautiful 
-https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 