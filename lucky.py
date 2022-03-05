#! python3
# lucky.py - Opens several Google Search Results

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select('.r a')

# Open a browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com/' + linkElems[i].get('href'))


# Get search keywords from command line arguments
# Retrieve the search results page
# Open a browser tab for each result
# Read the command line arguments from sys.argv
# Fetch the search result page with the requests module
# Find the links to each search result
# Call the webbrowser.open() to open the web browser