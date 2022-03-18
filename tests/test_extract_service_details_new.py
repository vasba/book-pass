import sys, os

sys.path.append('.')
sys.path.append('..')

from extract_service_details import extract_service_details


def test_extract_service_details():
    file = "/".join([os.path.realpath(os.path.dirname(__file__)), "test_data/reserved_time_details.html"])
    with open(file, "r") as f:
        content = f.read()
        details = extract_service_details(content)
        check = True
