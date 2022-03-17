import os
def load_database(notion):
  database = notion.databases.query(
    **{
      "database_id": os.getenv('DATABASE_ID'),
      "filter": {
        "property": "Status",
        "select": {
          "equals": "DONE"
        }
      }
    }
  )

  return database
