from django.shortcuts import render
import json
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import requests
# Create your views here.

def create_connection():
    """ create a database connection to the SQLite database """
    try:
        conn = sqlite3.connect('ETE_Etelä-Karjala.gpkg')
        return conn
    except Error as e:
        print(e)
 
    return None

def index(request):
    lat = request.GET['lat']
    lon = request.GET['lon']
    return render(request, 'index.html',{'lat':lat,'lon':lon})