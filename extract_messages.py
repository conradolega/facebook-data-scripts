import os
import pandas
from bs4 import BeautifulSoup

filename = '/home/conradolega/Downloads/facebook-data/messages/296.html'

with open(filename) as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    # Messages are archived in descending chronological order
    message_headers = soup.find_all('div', class_='message')
    message_headers.reverse()
    messages = [
        {
            'user': message_header.find('span', class_='user').text,
            'date': message_header.find('span', class_='meta').text,
            'message': message_header.next_sibling.text,
        }
        for message_header in message_headers]
    df = pandas.DataFrame.from_dict(messages)
    df.to_csv('messages.csv', encoding='utf-8')
