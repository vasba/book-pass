import sys, os

sys.path.append('.')
sys.path.append('..')

from boka_pass import earliest_time, regions

def test_earliest_time():
    region = regions[0]
    time = earliest_time(region)
    region = regions[1]
    time1 = earliest_time(region)
    check_time = True