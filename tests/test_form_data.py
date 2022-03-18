import datetime
import sys

sys.path.append('.')
sys.path.append('..')

from form_data import (iso, get_earliest_date, get_search_form, 
                       get_latest_date)

def test_iso():
    iso_date = iso(datetime.datetime.today())
    check = True

def test_get_earliest_date():
    date = get_earliest_date("ostergotland")
    check = True

def test_get_search_form():
    form = get_search_form("ostergotland")
    check = True

def test_get_latest_date():
    date = get_latest_date()
    check = True