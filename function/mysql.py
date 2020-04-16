import pymysql


def get_posts(length):
    """
    This function send request to ACF REST API.

    Args:
        length (int): Number of post you want to get (-1 for all posts)
        sql (str): What You Want to do
        data (tuple): What you get from the sql

    Returns:
        A Tuple.
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
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time ASC'
    else:
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time DESC ' + 'LIMIT ' + length

    # execute
    cursor.execute(sql)

    # 關閉連線
    connection.close()

    # all result
    data = cursor.fetchall()

    return_dict = data

    print("return:", return_dict[0])
    return return_dict


get_posts(-1)
