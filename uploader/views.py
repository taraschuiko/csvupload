from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadTableForm
from .people_table import PeopleTable

def index(request):
  form = UploadTableForm()
  return render(request, 'index.html', {'form': form})

def upload(request):
  if request.method == 'POST':
    form = UploadTableForm(request.POST, request.FILES)
    if form.is_valid():
      print("File is uploaded successfully", request.FILES['table'])
      table = PeopleTable(request.FILES['table'])
      table.sync_with_db()
  print(table.table)
  return render(request, 'success.html', {'stats': table.stats, 'people': table.table})