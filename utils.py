import json
import os
from requests import request
from requests.structures import CaseInsensitiveDict




def load_database(notion):
  database = notion.databases.query(
    **{
      'database_id': os.getenv('DATABASE_ID'),
      'filter': {
        'property': 'Status',
        'select': {
          'equals': 'DONE'
        }
      }
    }
  )

  return database

def update_page(notion, page_id, payload):
  headers = {
    'Authorization': f'Bearer {os.getenv("TOKEN")}',
    'Notion-version': '2022-02-22',
    'Content-type': 'application/json',
  }

  path = f'https://api.notion.com/v1/pages/{page_id}'

  return request(
    'PATCH',
    path,
    data=json.dumps({
      'properties': payload
    }),
    headers = headers,
  )

  # url = "https://api.notion.com/v1/pages/ef261ec1-fa7d-4b75-969a-9b541b99fa00"

  # payload = '''{
  #   "properties": {
  #     "select": {
  #       "name": "TO DO"
  #     }
  #   }
  # }'''

  # response = request("PATCH", url, json=payload, headers=headers)

  # print(response.text)

