from typing import List
import csv
import datetime
import sys

import requests


def cleanup_dict_keys(cases: List[dict]) -> List[dict]:
    """Normalizes Key Names."""
    mapper = {
        'Country_Region': 'Country/Region',
        'Province_State': 'State/Province',
        'Province/State': 'State/Province'
    }
    for case in cases:
        for k in mapper:
            if k in case:
                case[mapper[k]] = case[k]
                del case[k]
    return cases


def covid_cases_by_date(date: str) -> List[dict]:
    """Fetches list of cases for the given date."""
    url = f"https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv"

    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        print("Invalid date. Must be in format MM-DD-YYYY")
        sys.exit(1)

    response = requests.get(url)
    if not response:
        print("There was an error retrieving covid cases for the date provided.")
        sys.exit(1)

    # headers: Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
    cases = csv.DictReader(response.text.splitlines())
    next(cases)  # disgard header row
    cases = list(cases)
    cases = cleanup_dict_keys(cases)
    cases = sorted(cases, key=lambda c: (c['Country/Region'], c['State/Province']))
    return cases


if __name__ == '__main__':
    d = input('Enter date to search: ')
    for case in covid_cases_by_date(d):
        country_state = f"{case.get('Country/Region')} {case.get('State/Province')}"
        print(f"{d}: {case.get('Combined_Key', country_state)} - {case['Confirmed']} Confirmed - {case['Deaths']} Deaths - {case['Recovered']} Recovered")
