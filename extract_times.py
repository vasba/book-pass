from datetime import datetime
from lxml import html


def extract_times(content):
    doc = html.fromstring(content)
    times = doc.xpath(f"//*[@data-function='timeTableCell']")
    dates = []
    for time in times:
        sectionId = time.get('data-sectionid')
        servicetypeid = time.get('data-servicetypeid')
        fromdatetime = time.get('data-fromdatetime')
        dates.append((sectionId, servicetypeid,fromdatetime))
    dates.sort(key=lambda tup: tup[2]) 
    return dates

def get_earliest_valid_time(dates, latest_time):
    for date in dates:
        date_time = datetime.strptime(date[2], '%Y-%m-%d %H:%M:%S')
        if date_time < latest_time:
            return date
    return None