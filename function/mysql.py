import os
import pymysql
from dotenv import load_dotenv


def get_posts(length):
    """This function get post from old database.

    Args:
        length (int): Number of post you want to get (-1 for all posts)

    Returns:
        A Tuple.
        ex: ((category, title ,content, link, file), () ...)
    """
    load_dotenv()

    connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                 port=8080,
                                 user=os.getenv("DB_USER"),
                                 password=os.getenv("DB_PASSWORD"),
                                 db='hsnuwp',
                                 charset='utf8')

    # create cursor
    cursor = connection.cursor()

    # SQL
    if(length == -1):
        sql = 'SELECT msg_category, msg_title, msg_content, msg_link, msg_file \
                FROM wp_btaeon_msgs ORDER BY msg_time ASC'
    else:
        sql = 'SELECT msg_category, msg_title, msg_content, msg_link, msg_file \
                FROM wp_btaeon_msgs ORDER BY msg_time DESC LIMIT {}'.format(length)

    # execute
    cursor.execute(sql)

    # disconnect
    connection.close()

    # all result
    return cursor.fetchall()
