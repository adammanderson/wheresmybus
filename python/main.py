import time
import asyncio
import threading
import scrollphathd
from scrollphathd.fonts import font3x5
from os import getenv
import requests
from math import floor
from dotenv import load_dotenv
load_dotenv()

scrollphathd.rotate(degrees=180)
scrollphathd.set_brightness(0.2)

def seconds_to_minutes(seconds):
    return floor(seconds % 3600 / 60)

def format_minutes(minutes):
    return f'{minutes}m' if minutes > 0 else 'due'

def scroll_message(message):
        scrollphathd.clear()
        length = scrollphathd.write_string(message, x=1)
        scrollphathd.show()
        time.sleep(0.5)

        length -= scrollphathd.width

        while length > 0:
            scrollphathd.scroll(1)
            scrollphathd.show()
            length -= 1
            time.sleep(0.02)

        time.sleep(0.5)

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

async def get_stoppoint_arrivals():
    print('Fetching StopPoint Arrivals')
    endpoint = f'https://api.tfl.gov.uk/StopPoint/{getenv("STOPPOINT_ID")}/Arrivals'
    request = requests.get(endpoint, params={'app_id': getenv("API_APP_ID"), 'app_key': getenv("API_APP_KEY")})
    if request.status_code == 200:
        return request.json()
    else:
        print(f'error code {request.status_code}')
        scroll_message(f'error {request.status_code}')
        return []

async def format_arrivals(arrivals):
    if not arrivals:
        return 'No arrivals'

    line_name = arrivals[0]['lineName']
    arrivals.sort(key=lambda k: k['timeToStation'], reverse=True)
    mapped_arrivals = map(lambda x: format_minutes(seconds_to_minutes(x['timeToStation'])), arrivals)
    joined_arrivals = ' '.join(mapped_arrivals)
    
    print(joined_arrivals)
    return f'{line_name} {joined_arrivals}'

async def display_arrivals(value):
    print('Displaying arrivals')
    scroll_message(value)
    time.sleep(5)

async def main():
    while True:
        await display_arrivals(
            await format_arrivals(
                await get_stoppoint_arrivals()
            )
        )

if __name__== "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
