import asyncio
import scrollphathd
from os import getenv
import requests
from math import floor
from dotenv import load_dotenv
load_dotenv()

def seconds_to_minutes(seconds):
    return floor(seconds % 3600 / 60)

def format_minutes(minutes):
    return f'{minutes}m' if minutes > 0 else 'due'

async def get_stoppoint_arrivals():
    print('Fetching StopPoint Arrivals')
    await asyncio.sleep(1)
    endpoint = f'https://api.tfl.gov.uk/StopPoint/{getenv("STOPPOINT_ID")}/Arrivals'
    request = requests.get(endpoint, params={'app_id': getenv("API_APP_ID"), 'app_key': getenv("API_APP_KEY")})
    return request.json()


async def format_arrivals(arrivals):
    if len(arrivals) < 1:
        return 'No arrivals due'

    arrivals.sort(key=lambda k: k['timeToStation'], reverse=True)
    mapped_arrivals = map(lambda x: format_minutes(seconds_to_minutes(x['timeToStation'])), arrivals)
    joined_arrivals = ' | '.join(mapped_arrivals)
    return joined_arrivals

async def display_arrivals(value):
    scrollphathd.write_string(value)

async def main():
    await display_arrivals(
        await format_arrivals(
            await get_stoppoint_arrivals()
        )
    )

if __name__== "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
