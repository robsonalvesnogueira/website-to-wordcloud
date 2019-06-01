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
    html = get_url_contents(url)
    wordcloud = generate_word_cloud(html)
    save_word_cloud_to_image(wordcloud, 'wordcloud.png')

def generate_word_cloud(html):
    soup = BeautifulSoup(html, "html.parser")
    text = clean_html_text(soup.get_text())
    return WordCloud(background_color='white').generate(text)

def save_word_cloud_to_image(wordcloud, filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    wordcloud.to_file(folder+'/'+filename)
    return folder+filename

def clean_html_text(html):
    html = re.sub("\s+", ' ', html)
    html = re.sub("<.*?>", '', html)
    html = re.sub(r'\\n', ' ', html)
    return html

def get_url_contents(url):
    if (len(url) == 0):
        return 'Url not provided'
    if (not is_valid_url(url)):
        return 'Invalid url'
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    return str(urllib.request.urlopen(req).read().decode('utf-8'))

def is_valid_url(url):
    regex = re.compile(r'^(http|https)://', re.IGNORECASE)
    if re.match(regex, url):
        return True
    else:
        return False

if __name__ == "__main__":
    main()