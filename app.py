import os
import json
from datetime import datetime, timedelta
from notion_client import Client
from pprint import pprint


# notion = Client(auth='secret_T9UVf3PrsEmJ6QeMnGMBr30RTZ5RTUon2ayqMygjM7a')


# my_page = notion.databases.query(
#   **{
#     "database_id": '95e949f598ae4c9d9063bdb7a27438f9',
#     "filter": {
#       "property": "Status",
#       "select": {
#         "equals": "DONE"
#       }
#     }
#   }
# )

# with open('data.json', 'w') as f:
#   json.dump(my_page, f, indent=2)

status = [
  'TO DO',
  'DONE',
]

properties = [
  'Daily',
  '1t/w',
  '2t/w',
  '3t/w',

  '1t/2w',
  '1t/2m',
  '1t/3m',

  '1t/m',
  '2t/m',

  'On demand',

  'Mo',
  'Tue',
  'Wed',
  'Thu',
  'Fri',
]

day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

find_status = 'DONE'

due_date = '17:00'

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

        # print(set_date, due_date)

        # handle set date property
        if set_date > date_today:
          continue

        elif set_date < date_today:
          # get periodicity
          periodicity_property = properties['Periodicity']['multi_select']
          periodicity = []

          for i in periodicity_property:
            periodicity.append(i['name'])

          print(periodicity)



          # print(2)
          # print(due_date, ' <<< due_date')

        elif set_date == date_today:
          # set the task status as "To Do"
          # print(3)
          continue

