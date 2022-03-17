import os
import json
from datetime import datetime, timedelta
from calendar import monthrange
from notion_client import Client
from pprint import pprint
from utils import load_database


notion = Client(auth=os.getenv('TOKEN'))

# my_page = load_database(notion)

# with open('data.json', 'w') as f:
#   json.dump(my_page, f, indent=2)

day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

class GenDueDate:
  date = datetime.now()
  days_range = monthrange(date.year, date.month)

  weekdays = ['Daily', 'On demand', 'Mo', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Free']
  periodicity_times = ['1t', '2t', '3t', '4t', '5t', '6t']
  periodicity_range = ['m', '2m', '3m', 'w', '2w', '3w']
  periodicity_range_patters = {
    'm': days_range[1],
    'w': 7,
  }

  def __init__(self, periodicity_property):
    self.periodicity_source = periodicity_property
    self.periodicity_props = []

    # output data
    self.due_date = None
    self.set_date = None

    for i in periodicity_property:
      self.periodicity_props.append(i['name'])

    self.parse_periodicity()

    print(self.periodicity)

  def parse_periodicity(self):
    self.periodicity = {
      'days': [],
      'times': [],
      'range': None,
    }

    # parse periodicity range and times
    for i in self.periodicity_props:
      if i in self.weekdays:
        if i != 'Daily':
          self.periodicity['days'].append(self.weekdays.index(i))

        else:
          self.periodicity['days'].append(i)
          break

      else:
        periodicity_and_range = i.split('/')

        if len(periodicity_and_range) > 1:
          if periodicity_and_range in self.periodicity_range:
            self.periodicity['range'] = periodicity_and_range[0]
            self.periodicity['times'].append(periodicity_and_range[1][0])

          else:
            self.periodicity['range'] = periodicity_and_range[1]
            self.periodicity['times'].append(periodicity_and_range[0][0])

        else:
          self.periodicity['days'] = periodicity_and_range[0]

      self.periodicity['days'].sort()

  def generate_day(self, count, ):
    weekday_number = self.weekdays.index(self.date.weekday)

    for periodicity_day in self.periodicity['days']:
      if (periodicity_day > weekday_number):
        pass

  def generate_due_date(self):
    if len(self.periodicity['days']) != 0:
      weekday_number = self.weekdays.index(self.date.weekday)

      if self.periodicity['times'] == 1:
        pass

      # for periodicity_day in self.periodicity['days']:
      #   if (periodicity_day > weekday_number):


    # else:
    #   pass

  def generate_set_date(self):
    if 'Daily' in self.periodicity['days']:
      self.set_date = self.due_date

    else:
      if len(self.periodicity['times']) == 0:
        for i in self.periodicity['range']:
          if i == 'm' or i == 'w':
            self.set_date = datetime(self.due_date.year, self.due_date.month, self.due_date.day - 7)

      else:
        for i in self.periodicity['range']:
          if i == 'm' or i == 'w':
            self.set_date = datetime(self.due_date.year, self.due_date.month, self.due_date.day - 14)

with open('data.json', 'r') as f:
  my_page = json.load(f)

  date_today = datetime(
    datetime.now().year,
    datetime.now().month,
    datetime.now().day,
  )

  day_name = day_names[date_today.weekday()]

  for page in my_page['results']:
    properties = page['properties']

    if properties['Set date']['date']:
      if 'start' in properties['Set date']['date']:
        set_date_start = list(map(int, properties['Set date']['date']['start'].split('-')))
        set_date = datetime(*set_date_start)
        due_date_property = list(map(int, page['properties']['Due Date']['date']['start'].split('-')))
        due_date = datetime(*due_date_property)

        # handle set date property
        if set_date > date_today:
          continue

        elif set_date < date_today:
          # get periodicity
          x = GenDueDate(properties['Periodicity']['multi_select'])

          # print(due_date, ' <<< due_date')

        elif set_date == date_today:
          # set the task status as "To Do"
          # print(3)
          continue
