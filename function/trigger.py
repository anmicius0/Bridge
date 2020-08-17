import os
import pymysql
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

    # get number of posts
    connection = pymysql.connect(host="140.131.149.23",
                                 port=8080,
                                 user="root",
                                 password="cnmc",
                                 db='hsnuwp',
                                 charset='utf8')

    cursor = connection.cursor()
    sql = 'SELECT COUNT(*) FROM wp_btaeon_msgs'
    cursor.execute(sql)
    connection.close()
    post_number = int(cursor.fetchone()[0])

    # set variable
    limit = 200
    urls = ("https://us-central1-digital-layout-286410.cloudfunctions.net/bridge?nth={0}".format(
        i) for i in range(post_number * (-1)))

    # the coroutine
    async def fetch(url, session):
        # print what's happening now
        print(f"{url} triggered")

        # send request every 0.1s
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


if __name__ == "__main__":
    trigger()
