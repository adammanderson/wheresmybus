import asyncio
from services import Arrivals
from utils import set_interval
from dotenv import load_dotenv
load_dotenv()

service_list = {
    'arrivals': Arrivals().get_stoppoint
}

async def main():
    active_service = 'arrivals'
    set_interval(service_list[active_service], 10)

if __name__== "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
