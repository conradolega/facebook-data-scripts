import os
import pandas
from bs4 import BeautifulSoup

directory = ''
threads_data = []

def extract_messages(filepath):
    with open(filepath) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        chat_name = soup.title.text.split('Conversation with ')[1]
        # Messages are archived in descending chronological order
        message_headers = soup.find_all('div', class_='message')
        message_headers.reverse()
        messages = [{'user': message_header.find('span').text, 'message': message_header.next_sibling.text} for message_header in message_headers]
        threads_data.append({'chat_name': chat_name, 'message_count': len(messages)})

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        extract_messages(os.path.join(directory, filename))

df = pandas.DataFrame.from_dict(threads_data)
df.to_csv('threads.csv', encoding='utf-8')
