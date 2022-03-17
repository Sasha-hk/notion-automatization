import json
import os
import requests
from datetime import datetime, timedelta
from notion_client import Client
from utils import load_database


notion = Client(auth=os.getenv('TOKEN'))

# my_page = load_database(notion)

# with open('data.json', 'w') as f:
#   json.dump(my_page, f, indent=2)

days_periodicity = ['Mo', 'Tue', 'Wed', 'Thu', 'Fri']
special_days_property = ['Daily', 'On demand']
periodicity_ranges = ['1t/w', '2t/w', '3t/w', '1t/2w', '1t/m', '2t/m', '2t/m', '1t/2m', '1t/3m']



with open('data.json', 'r') as f:
  my_page = json.load(f)

  date_today = datetime(
    datetime.now().year,
    datetime.now().month,
    datetime.now().day,
  )

  day = date_today.weekday()

  for page in my_page['results']:
    properties = page['properties']

    if properties['Set date']['date']:
      if 'start' in properties['Set date']['date']:
        set_date_start = list(map(int, properties['Set date']['date']['start'].split('-')))
        set_date = datetime(*set_date_start)
        due_date_property = list(map(int, page['properties']['Due Date']['date']['start'].split('-')))
        due_date = datetime(*due_date_property)
        result_set_date = None
        result_due_date = None

        # handle set date property
        if set_date > date_today:
          continue

        elif set_date < date_today:
          due_date_property = list(map(int, properties['Due Date']['date']['start'].split('-')))
          due_date = datetime(*due_date_property)
          set_date_property = list(map(int, properties['Set date']['date']['start'].split('-')))
          set_date = datetime(*set_date_property)
          periodicity_property = properties['Periodicity']['multi_select']
          periodicity = [i['name'] for i in periodicity_property]
          print('==========================')

          # set due date
          if 'Daily' in periodicity:
            result_due_date = date_today

          else:
            next_date = None

            for i in periodicity:
              if i in days_periodicity:
                if due_date.weekday() < days_periodicity.index(i):
                  next_date = due_date.day + (days_periodicity.index(i) - due_date.weekday())

            if not next_date:
              for i in periodicity:
                if i in days_periodicity:
                  next_date = due_date.day + (6 - due_date.weekday()) + days_periodicity.index(i)
                  break

            if next_date:
              result_due_date = datetime(due_date.year, due_date.month, next_date)


          # set set date
          if result_due_date:
            for i in periodicity:
              if i == 'Daily':
                result_set_date = result_due_date
                break

              else:
                if i in periodicity_ranges:
                  range_parts = i.split('/')

                  if range_parts[1] == 'w':
                    result_set_date = datetime(result_due_date.year, result_due_date.month, result_due_date.day - 1)
                    break

                  elif range_parts[1] == 'm':
                    result_set_date = datetime(result_due_date.year, result_due_date.month, result_due_date.day - 7)
                    break

                  elif range_parts[1] == '2w' or range_parts[1] == '3m':
                    result_set_date = datetime(result_due_date.year, result_due_date.month, result_due_date.day - 14)
                    break

          print(result_due_date, result_set_date)


        elif set_date == date_today:
          # set status as To Do
          continue
