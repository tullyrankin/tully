import datetime

import fire

from tully import __version__ as version
import tully.covid19 as covid19
import tully.network as network

VERSION_FANCY = f"""\
 _____     _ _
|_   _|  _| | |_  _
  | || || | | | || |
  |_| \_,_|_|_|\_, |
               |__/
Version: {version}"""


class Covid19Cli:
    def cases_by_date(self, date: str = None):
        """Retrieves COVID19 cases for today or given date provided."""
        if not date:
            date = datetime.datetime.now().strftime('%m-%d-%Y')
        for case in covid19.covid_cases_by_date(date):
            country_state = (
                f"{case.get('Country/Region')} "
                f"{case.get('State/Province')}"
            )
            print(f"{date}: {case.get('Combined_Key', country_state)} "
                  f"- {case['Confirmed']} Confirmed - {case['Deaths']} "
                  f"Deaths - {case['Recovered']} Recovered")


class NetworkCli:
    def __init__(self):
        self.host = network.host_ip
        self.ip = network.ip
        self.nics = network.nics


class Cli:
    def __init__(self):
        self.covid19 = Covid19Cli
        self.network = NetworkCli
        self.version = lambda: VERSION_FANCY


def main():
    fire.Fire(Cli)
