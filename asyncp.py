from aiohttp import ClientSession, TCPConnector
import asyncio
import sys
import pypeln as pl
import timeit
import time

limit = 1000
urls = ("https://example.com" for i in range(10000))


async def fetch(url, session):
    time.sleep(0.1)
    async with session.get(url) as response:
        text = await response.text()
        print(text)


pl.task.each(
    fetch,
    urls,
    workers=limit,
    on_start=lambda: dict(session=ClientSession(
        connector=TCPConnector(limit=None))),
    on_done=lambda session: session.close(),
    run=True,
)
