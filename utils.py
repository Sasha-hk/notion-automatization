def load_database(notion):
  database = notion.databases.query(
    **{
      "database_id": '95e949f598ae4c9d9063bdb7a27438f9',
      "filter": {
        "property": "Status",
        "select": {
          "equals": "DONE"
        }
      }
    }
  )

  return database
