import asyncio
import aiofiles
import aiohttp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action="store")
args = parser.parse_args()

async def get_content():
    async with aiohttp.ClientSession() as session:
        async with session.get() as resp:
            resp = await resp.read()
            # resp contient le contenu HTML de la page
            print(resp)


get_content()

