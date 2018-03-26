import os
from bs4 import BeautifulSoup

filename = ''

with open(filename) as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    messages = [message.text for message in soup.find_all('p').reverse()]
