from django.shortcuts import render
import requests
import json 
from typing import List, final
from collections import Iterable
from django.http import HttpResponse
import re
from bs4 import BeautifulSoup
import csv
import pandas as pd
from json import loads
import requests
from time import time
import glob
import os
from django.http import JsonResponse

# Create your views here.


def get_key_ratio(ticker,market):
    headers = {
        'Referer': 'http://financials.morningstar.com/ratios/r.html?t=EXPE&region=usa&culture=en-US',
        }
    stockmarket = market.GET.get('market')
    stockmarket = stockmarket.replace(" ", "+")
    stockticker = ticker.GET.get('ticker')
    stockticker = stockticker.replace(" ", "+")
    screen = requests.get(f"http://financials.morningstar.com/finan/ajax/exportKR2CSV.html?&callback=?&t={stockmarket}:{stockticker}&region=usa&culture=en-US&cur=&order=asc", headers=headers)
    return screen






def get_stock_income_statement(ticker,market):
    headers = {
        'Referer': 'http://financials.morningstar.com/ratios/r.html?t=EXPE&region=usa&culture=en-US',
        }
    stockmarket = market.GET.get('market')
    stockmarket = stockmarket.replace(" ", "+")
    stockticker = ticker.GET.get('ticker')
    stockticker = stockticker.replace(" ", "+")
    screen = requests.get(f"http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t={stockmarket}:{stockticker}&region=usa&culture=en-US&cur=&reportType=is&period=12&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=13805&denominatorView=raw&number=3", headers=headers)
    return screen

def get_stock_cash_flow(ticker,market):
    headers = {
        'Referer': 'http://financials.morningstar.com/ratios/r.html?t=EXPE&region=usa&culture=en-US',
        }
    stockmarket = market.GET.get('market')
    stockmarket = stockmarket.replace(" ", "+")
    stockticker = ticker.GET.get('ticker')
    stockticker = stockticker.replace(" ", "+")
    screen = requests.get(f"http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t={stockmarket}:{stockticker}&region=usa&culture=en-US&cur=&reportType=cf&period=12&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=13805&denominatorView=raw&number=3", headers=headers)
    return screen  


def cash_flow_json(request):
    if 'ticker' in request.GET and 'market' in request.GET:
        os.remove("testy.csv")
        html_content = get_stock_cash_flow(request, request)
        csv = html_content.content
        with open("newcsv.csv", "wb") as file:
            file.write(csv)
        file.close()

        header_name = ["name","year_six","year_seven","year_eigth","year_nine","year_ten","year_ttm","yearsss"]


        
        file1 = open("testy.csv", "a")
        file2 = open("newcsv.csv", "r")
        file1.write(",".join(header_name))

        for line in file2:
            file1.write(line)

        file1.close()
        file2.close()


        rows_to_keep = [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    
        df = pd.read_csv ('testy.csv', skiprows = lambda x: x not in rows_to_keep)
        df.replace(',','', regex=True, inplace=True)
        df.to_json ('jsonfile.json', orient='records')
        a_file = open("jsonfile.json", "r")
        a_json = json.load(a_file)
        pretty_json = json.dumps(a_json).replace("null", '"0"')
        a_file.close()
        
    return HttpResponse(pretty_json, content_type='text/json')


def income_statement_json(request):
    if 'ticker' in request.GET and 'market' in request.GET:
        os.remove("testy.csv")
        html_content = get_stock_income_statement(request, request)
        csv = html_content.content
        with open("newcsv.csv", "wb") as file:
            file.write(csv)
        file.close()

        header_name = ["name","year_six","year_seven","year_eigth","year_nine","year_ten","year_ttm","yearsss"]


        
        file1 = open("testy.csv", "a")
        file2 = open("newcsv.csv", "r")
        file1.write(",".join(header_name))

        for line in file2:
            file1.write(line)

        file1.close()
        file2.close()


        rows_to_keep = [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    
        df = pd.read_csv ('testy.csv', skiprows = lambda x: x not in rows_to_keep)
        df.replace(',','', regex=True, inplace=True)
        df.to_json ('jsonfile.json', orient='records')
        a_file = open("jsonfile.json", "r")
        a_json = json.load(a_file)
        pretty_json = json.dumps(a_json).replace("null", '"0"')
        a_file.close()
        
    return HttpResponse(pretty_json, content_type='text/json')



def stock_history_key_ratio_json(request):
    if 'ticker' in request.GET and 'market' in request.GET:
        os.remove("testy.csv")
        html_content = get_key_ratio(request, request)
        csv = html_content.content
        with open("newcsv.csv", "wb") as file:
            file.write(csv)
        file.close()

        header_name = ["name", "year_one", "year_two","year_three","year_four","year_five","year_six","year_seven","year_eigth","year_nine","year_ten","year_ttm","yearsss"]


        
        file1 = open("testy.csv", "a")
        file2 = open("newcsv.csv", "r")
        file1.write(",".join(header_name))

        for line in file2:
            file1.write(line)

        file1.close()
        file2.close()


        rows_to_keep = [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    
        df = pd.read_csv ('testy.csv', skiprows = lambda x: x not in rows_to_keep)
        df.replace(',','', regex=True, inplace=True)
        df.to_json ('jsonfile.json', orient='records')
        a_file = open("jsonfile.json", "r")
        a_json = json.load(a_file)
        pretty_json = json.dumps(a_json).replace("null", '"0"')
        # parsed_data = json.loads(pretty_json)
        a_file.close()
        
    return HttpResponse(pretty_json, content_type='text/json')
