import pymysql


def get_posts(length):
    """This function get post from old database.

    Args:
        length (int): Number of post you want to get (-1 for all posts)

    Returns:
        A Tuple.
        ex: ((category, title ,content, link, file), () ...)
    """

    # set connect path
    host = 'shen.bike'
    port = 8080
    user = 'root'
    passwd = 'cnmc'
    db = 'hsnuwp'
    charset = 'utf8'

    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=passwd,
                                 db=db,
                                 charset=charset)

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

    # all result
    data = cursor.fetchall()

    # disconnect
    connection.close()

    return data
