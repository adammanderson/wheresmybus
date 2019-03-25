import requests
import time
from os import getenv
from utils import format_minutes, seconds_to_minutes, scroll_message

class Arrivals:
    def get_stoppoint(self):
        print('Arrivals: Requesting StopPoint')
        request = requests.get(
            f'https://api.tfl.gov.uk/StopPoint/{getenv("STOPPOINT_ID")}/Arrivals',
            params={'app_id':getenv("TFL_API_ID"), 'app_key': getenv("TFL_API_KEY")}
        )

        if request.status_code == 200:
            self.__format_arrivals(request.json())
        else:
            scroll_message(f'error {request.status_code}')
            return

    def __format_arrivals(self, arrivals):
        if not arrivals:
            return 'No arrivals'

        line_name = arrivals[0]['lineName']
        arrivals.sort(key=lambda k: k['timeToStation'], reverse=True)
        mapped_arrivals = map(lambda x: format_minutes(seconds_to_minutes(x['timeToStation'])), arrivals)
        joined_arrivals = ' '.join(mapped_arrivals)
        formatted = f'{line_name} {joined_arrivals}'

        scroll_message(f'{line_name} {joined_arrivals}')
        return
