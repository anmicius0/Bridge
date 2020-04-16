import pymysql


def get_posts(length):
    """
    This function send request to ACF REST API.

    Args:
        length (int): Number of post you want to get (0 for all posts)

    Returns:
        A Tuple of all posts you want.
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
    if(length == 0):
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time ASC'
    else:
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time DESC ' + \
            'LIMIT ' + str(length)

    # execute
    cursor.execute(sql)

    # disconnect
    connection.close()

    # all result
    data = cursor.fetchall()

    return_dict = data

    return return_dict


print("return:", get_posts(0))
