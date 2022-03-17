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

def update_page(notion, page_id, data):
  notion.pages.update(
    page_id,
    data,
  )
