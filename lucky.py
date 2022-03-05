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
