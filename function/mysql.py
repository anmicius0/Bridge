import os
import pymysql
from dotenv import load_dotenv


def get_post(nth):
    """This function get 1 post from old database.

    Args:
        nth (int): Nth post you want to get (like python, can use 0, -1 etc.)

    Returns:
        A Tuple.
        ex: (category, title ,content, link, file)
    """
    load_dotenv()

    connection = pymysql.connect(host="140.131.149.23",
                                 port=8080,
                                 user="root",
                                 password="cnmc",
                                 db='hsnuwp',
                                 charset='utf8')

    # create cursor
    cursor = connection.cursor()

    # SQL
    if(nth >= 0):
        sql = f'SELECT msg_category, msg_title, msg_content, msg_link, msg_file \
                FROM wp_btaeon_msgs ORDER BY msg_time DESC LIMIT {nth}, 1'
    else:
        sql = f'SELECT msg_category, msg_title, msg_content, msg_link, msg_file \
                FROM wp_btaeon_msgs ORDER BY msg_time ASC LIMIT {abs(nth)-1}, 1'

    # execute
    cursor.execute(sql)

    # disconnect
    connection.close()

    # all result
    return cursor.fetchone()
