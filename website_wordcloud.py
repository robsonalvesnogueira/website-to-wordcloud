# coding: utf-8
import sys
import re
import os
import urllib
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def main():
    url = '' if len(sys.argv) == 1 else sys.argv[1]
    html = getUrlContents(url)
    wordcloud = generateWordcloud(html)
    saveWordcloudToImage(wordcloud, 'wordcloud.png')

def generateWordcloud(html):
    soup = BeautifulSoup(html, "html.parser")
    text = cleanHtmlText(soup.get_text())
    return WordCloud(background_color='white').generate(text)

def saveWordcloudToImage(wordcloud, filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    wordcloud.to_file(folder+'/'+filename)
    return folder+filename

def cleanHtmlText(html):
    html = re.sub("\s+", ' ', html)
    html = re.sub("<.*?>", '', html)
    html = re.sub(r'\\n', ' ', html)
    return html

def getUrlContents(url):
    if (len(url) == 0):
        return 'Url not provided'
    if (not isValidUrl(url)):
        return 'Invalid url'
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    return str(urllib.request.urlopen(req).read().decode('utf-8'))

def isValidUrl(url):
    regex = re.compile(r'^(http|https)://', re.IGNORECASE)
    if re.match(regex, url):
        return True
    else:
        return False

if __name__ == "__main__":
    main()