import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

def csv_reader(file):
    with open(file, encoding='utf-8') as csv_file:
        content = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            content.append(row)
    return content

def bus_stations(request):
    CONTENT = csv_reader(BUS_STATION_CSV)
    paginator = Paginator(CONTENT, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
