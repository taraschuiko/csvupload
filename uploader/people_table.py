from .helpers.csv_string_parse import csv_string_parse

class PeopleTable:
  table = ''

  def __init__(self, csv_file):
    parsed_csv = csv_string_parse(str(csv_file.read()))
    print(parsed_csv)

  def load_to_db(self, parameter_list):
    pass