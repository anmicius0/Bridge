import os
import pymysql
from dotenv import load_dotenv
from aiohttp import ClientSession, TCPConnector
import asyncio
import sys
import pypeln as pl
import time


def trigger():
    """This function trigger import process for all post.

    Returns:
        A Tuple.
        ex: (category, title ,content, link, file)
    """
    load_dotenv()

    # get number of posts
    connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                 port=8080,
                                 user=os.getenv("DB_USER"),
                                 password=os.getenv("DB_PASSWORD"),
                                 db='hsnuwp',
                                 charset='utf8')
    cursor = connection.cursor()
    sql = 'SELECT COUNT(*) FROM wp_btaeon_msgs'
    cursor.execute(sql)
    connection.close()
    post_number = int(cursor.fetchone()[0])

    # set variable
    limit = 1000
    urls = ("https://us-central1-hsnu-org-274410.cloudfunctions.net/import?nth={0}".format(
        i) for i in range(post_number))

    # the coroutine
    async def fetch(url, session):
        time.sleep(0.1)
        async with session.get(url) as response:
            text = await response.text()
            print(text)

    # execute coroutine
    pl.task.each(
        fetch,
        urls,
        workers=limit,
        on_start=lambda: dict(session=ClientSession(
            connector=TCPConnector(limit=None))),
        on_done=lambda session: session.close(),
        run=True,
    )
