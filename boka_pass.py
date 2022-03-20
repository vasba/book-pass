import datetime, os, re, time, requests

from form_data import (get_search_form, get_first_data, second_step, 
                       third_step, get_latest_date, get_reserv_form, get_details_form, 
                       just_next, book_form, bekrafta_bokning)
from extract_times import extract_times, get_earliest_valid_time
from extract_service_details import extract_service_details
from check_boking_done import check_boking_done

#region_pairs = [(56, 'ostergotland'), (17, 'orebro'), (59, 'jonkoping'), (60, 'sodermanland'), (47, 'stockholm')]
region_pairs = [(56, 'ostergotland')]
#region_pairs = [(47, 'stockholm'), (60, 'sodermanland')]

BASE_URL = "https://bokapass.nemoq.se/Booking/Booking"
FORM_URL = BASE_URL + "/Index/ostergotland"
POST_URL = BASE_URL + "/Next/ostergotland"

def get_form_url(region):
    return f"{BASE_URL}/Index/{region}"

def get_post_url(region):
    return f"{BASE_URL}/Next/{region}"

FIrstname = ""
last_name = ""
email = ""
PHone = ""

Sections_ids = {
    90: "Linköping",
    91: "Motala",
    92: "Norrköping",
    38: "Flemingsberg",
    41: "Sthlm city"
    }

def has_error(r, should_exit=False):
    if not r.ok:
        print(r, r.headers)
    s = 'alert-error'
    s1 = 'Felsida'
    if s in r.text:
        print(r.text.split(s)[1].split('<div>')[0])
        #say("error")
        if should_exit:
            raise Exception(r.request.body)
        else:
            return True
    try:
        r.raise_for_status()
    except Exception as e:
        return True

def say(text):
    os.system(f"say {text!r}")


preffered_section_ids = [90, 38, 41]
booked_time = False
found_times = []
best_time = None

def get_best_time(found_times):
    found_times.sort(key=lambda tup: tup[1][2])
    return found_times[0]

while not booked_time:
    time.sleep(60)
    try:
        for region_pair in region_pairs:
            region = region_pair[1]
            region_id = region_pair[0]
            session = requests.Session()
            session.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'})

            r1 = requests.get(get_form_url(region))
            with open(f"start_{region}.html", "w")as f:
                f.write(r1.text)
            if has_error(r1):
                continue;

            result = session.post(get_post_url(region), get_first_data(region_id),
                              allow_redirects=True,
                              cookies=r1.cookies)
            with open(f"first_{region}.html", "w")as f:
                f.write(result.text)
            if has_error(result):
                continue;

            result = session.post(get_post_url(region), second_step,
                      allow_redirects=True,
                      cookies=r1.cookies)
            with open(f"second_{region}.html", "w")as f:
                f.write(result.text)

            if has_error(result):
                continue;

            result = session.post(get_post_url(region), third_step,
                      allow_redirects=True,
                      cookies=r1.cookies)

            with open(f"third_{region}.html", "w")as f:
                f.write(result.text)

            if has_error(result):
                continue;

            result = session.post(get_post_url(region), 
                                  get_search_form(region),
                                  allow_redirects=True,
                                  cookies=r1.cookies)

            with open(f"found_times_{region}.html", "w")as f:
                f.write(result.text)

            if has_error(result):
                continue;
            else:
                dates = extract_times(result.text)
                earliest_valid_time = get_earliest_valid_time(dates, get_latest_date())
                if earliest_valid_time and '90' in earliest_valid_time[0]:
                #if earliest_valid_time:
                    found_times.append((region_pair, earliest_valid_time, session, r1.cookies))

            #if len(found_times) > 0:
            #    best_time = get_best_time(found_times)

            if len(found_times) > 0:
                for best_time in found_times:
                    best_time_session = best_time[2]
                    best_time_cokies = best_time[3]
                    best_time_region = best_time[0][1]
                    region = best_time_region
                    sectionId = best_time[1][0]
                    servicetypeid = best_time[1][1]
                    fromdatetime = best_time[1][2]

                    reservation_form = get_reserv_form(sectionId, servicetypeid, fromdatetime)
                    result = best_time_session.post(get_post_url(best_time_region), 
                               reservation_form,
                                allow_redirects=True,
                                cookies=best_time_cokies)

                    with open(f"reserved_{region}.html", "w")as f:
                        f.write(result.text)

                    if has_error(result):
                        continue;

                    try:
                        first_service_id, first_service_name, second_service_id, second_service_name = extract_service_details(result.text)
                    except Exception as e:
                        continue

                    result = best_time_session.post(get_post_url(best_time_region),
                               get_details_form(first_service_id, first_service_name,
                                                second_service_id, second_service_name),
                                allow_redirects=True,
                                cookies=best_time_cokies)

                    with open(f"reservation_details_{region}.html", "w")as f:
                        f.write(result.text)

                    if has_error(result):
                        continue;

                    result = best_time_session.post(get_post_url(best_time_region), 
                               just_next,
                                allow_redirects=True,
                                cookies=best_time_cokies)

                    with open(f"confirm_reservation_{region}.html", "w")as f:
                        f.write(result.text)

                    if has_error(result):
                        continue;

                    result = best_time_session.post(get_post_url(best_time_region), 
                               book_form,
                                allow_redirects=True,
                                cookies=best_time_cokies)

                    with open(f"book_{region}.html", "w")as f:
                        f.write(result.text)

                    if has_error(result):
                        continue;

                    result = best_time_session.post(get_post_url(best_time_region), 
                               bekrafta_bokning,
                                allow_redirects=True,
                                cookies=best_time_cokies)

                    with open(f"bekrafta_bokning_{region}.html", "w")as f:
                        f.write(result.text)

                    boking = check_boking_done(result.text)
                    if boking:
                        booked_time = True

                    if has_error(result):
                        continue;

    except Exception as e:
        continue

check_result = True
