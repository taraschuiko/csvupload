from .helpers.csv_string_parse import csv_string_parse
from .models import Person
import datetime

class PeopleTable:
  table = []
  stats = {
    'added': 0,
    'updated': 0,
    'removed': 0
  }

  def __init__(self, csv_file):
    self.table = csv_string_parse(str(csv_file.read()))

  def sync_with_db(self):
    for person in self.table:
      # Add
      if not len(Person.objects.filter(uid = person['uid'])):
        Person(
          uid = person['uid'],
          first_name = person['firstName'],
          last_name = person['lastName'],
          birth_day = person['birthDay'],
          date_change = person['dateChange'],
          description = person['description'],
        ).save()
        self.stats['added'] += 1
      # Update
      if len(Person.objects.filter(
        uid = person['uid']
      ).exclude(
        date_change__contains = person['dateChange']
      )):
        Person.objects.filter(uid = person['uid']).update(
          first_name = person['firstName'],
          last_name = person['lastName'],
          birth_day = person['birthDay'],
          date_change = person['dateChange'],
          description = person['description'],
        )
        self.stats['updated'] += 1
    # Remove
    for person_db in Person.objects.all():
      remove = True
      for person_table in self.table:
        if person_db.uid == person_table['uid']: remove = False
      if remove:
        person_db.delete()
        self.stats['removed'] += 1