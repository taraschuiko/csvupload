import re

def csv_string_parse(csv_string):
  csv_rows = csv_string.split('\\r\\n')
  csv_items = []
  for i in range(len(csv_rows)):
    csv_items.append(csv_rows[i].split(';'))
  csv_items.pop()

  keys = csv_items[0]
  del csv_items[0]

  rows = []

  for i in range(len(csv_items)):
    rows.append({})
    for j in range(len(csv_items[0])):
      if bool('b\'' in keys[j]): keys[j] = keys[j].replace('b\'', '')
      rows[i][keys[j]] = csv_items[i][j]
  
  return rows