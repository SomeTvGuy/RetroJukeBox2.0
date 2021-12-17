# Retro-Jukebox
A simple Music Downloader for Kinder
Roughly inspired by the same kind of project by [@obskyr](https://github.com/obskyr/khinsider)

# NOTE
**You need requests and beautiful soup in order to make this script work**  this was also made in Python so please ensure that you have that installed too
To install requests, all you need to do is open cmd or whatever the equivalent of terminal si for your OS and put in the following command:
"Pip install requests"
"Python -m pip install requests
You May also need to install Beautiful Soup 4 as well, using a similar command as well, I'll link the documentation below just in case you have any difficulty

# Brief Background
This is essentially just a web scraper built to download files one by one from the KhInsider website. The goal of this project was to successfully bypass the paywall downloading videogame soundtracks as an album, as their main gimmick behind running their site is donating to them to mass download whole albums. While I don't know too much about who owns the licensing on the website, it is true that anyone can download each song individually for free without paying them a dime.I'd also like to note that through my testing, none of the GET requests have returned a response code above 200, from what I heard that means that it's **OK** to do this, not too sure though.

The requests module used within this project is used in order to send "GET" requests to sort through the pages HTML, find the URL attached to each track's name, then continuously follow each URL until they get to the download link for each individual file. Beautiful soup is used to parse through the elements of the given URL and is used in conjunction with regex in order to properly differentiate between the song names, timestamps, and file size.

# How To Run
-Make sure you're connected to some sort of Wi-fi

-Ensure that you have both the BeatifulSoup and the Requests library installed on your machine. This goes without saying, but also make sure you have the Latest Version of Python installed on your machine as well

-Open the 'RetroJukeBox.py' file in your favorite IDE, and run the file!

-There will be a message in the terminal window saying 'Please Enter In A Valid Khinsider Album Url: ', copy and paste a URL from the website, and press enter

-You'll be asked to provide an album name,**this is the name of the Folder that your tracks will be held in**. I'd recommend storing it as the name of the videogame or maybe something unique to prevent any errors from going on


# References
**Raw String to HTML**
https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
"""
Import re
as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext
"""

**Requests**
-https://docs.python-requests.org/

**Beautiful** 
-https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 