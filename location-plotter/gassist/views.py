from django.shortcuts import render
import json
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests
# Create your views here.

def index(request):
    lat = request.GET['lat']
    lon = request.GET['lon']
    return render(request, 'index.html',{'lat':lat,'lon':lon})