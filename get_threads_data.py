import os
import pandas
from bs4 import BeautifulSoup

directory = '/home/conradolega/Downloads/facebook-data/messages'
threads_data = []

def get_threads_data(filepath):
    with open(filepath) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        chat_name = soup.title.text.split('Conversation with ')[1]
        message_headers = soup.find_all('div', class_='message')
        threads_data.append({'chat_name': chat_name, 'message_count': len(message_headers)})

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        get_threads_data(os.path.join(directory, filename))

df = pandas.DataFrame.from_dict(threads_data)
df.to_csv('threads_data.csv', encoding='utf-8')
