import matplotlib.pyplot
import pandas
from dateutil.parser import parse

filename = 'messages.csv'

def convert_to_date(message):
    return parse(message.date).date()
   

message_dates = pandas.read_csv(filename).apply(convert_to_date, axis=1)
messages_by_date = message_dates.groupby(message_dates).count()
matplotlib.pyplot.show(messages_by_date.plot())
