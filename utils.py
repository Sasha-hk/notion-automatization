import json
import os
from requests import request


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

def update_page(page_id, payload):
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
