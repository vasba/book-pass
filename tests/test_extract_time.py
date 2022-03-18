from datetime import datetime
import sys, os

sys.path.append('.')
sys.path.append('..')

from extract_times import extract_times, get_earliest_valid_time


def test_extract_times():
    file = "/".join([os.path.realpath(os.path.dirname(__file__)), "test_data/found_times.html"])
    with open(file, "r") as f:
        content = f.read()
        dates = extract_times(content)
        latest = datetime.strptime("2022-10-11 11:40:00", '%Y-%m-%d %H:%M:%S')
        time = get_earliest_valid_time(dates, latest)
        assert time

