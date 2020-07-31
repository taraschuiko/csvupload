from .helpers.csv_string_parse import csv_string_parse
from .models import Person

class PeopleTable:
  table = []

  def __init__(self, csv_file):
    self.table = csv_string_parse(str(csv_file.read()))
    print(self.table)

  def load_to_db(self):
    for person in self.table:
      Person(
        uid = person['uid'],
        first_name = person['firstName'],
        last_name = person['lastName'],
        birth_day = person['birthDay'],
        date_change = person['dateChange'],
        description = person['description'],
      ).save()

    print(Person.objects.all())