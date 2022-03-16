import os
import json
from datetime import datetime, timedelta
from notion_client import Client
from pprint import pprint


# notion = Client(auth='secret_T9UVf3PrsEmJ6QeMnGMBr30RTZ5RTUon2ayqMygjM7a')

# # # list_users_response = notion.users.list()
# # # print(list_users_response)

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

find_status = 'DONE'


due_date = '17:00'

with open('data.json', 'r') as f:
  my_page = json.load(f)

  date_today = datetime(
    datetime.now().year,
    datetime.now().month,
    datetime.now().day,
  )


  for page in my_page['results']:
    properties = page['properties']

    # print(page, ' <<<< ')
    # check if set date exists and handle the value
    if properties['Set date']['date']:
      # print(properties['Set date']['date'])
      if 'start' in properties['Set date']['date']:
        set_date_property = list(map(int, properties['Set date']['date']['start'].split('-')))
        set_date = datetime(set_date_property[0], set_date_property[1], set_date_property[2])


        # handle set date property
        if set_date > date_today:
          continue

        elif set_date < date_today:
          due_date = properties['Priority']['select']['name']
          print(due_date, ' <<< due_date')
          print(2)

        elif set_date == date_today:
          print(3)

