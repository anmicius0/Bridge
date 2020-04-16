import pymysql

# set connect path
host = 'shen.bike'
port = 8080
user = 'root'
passwd = 'cnmc'
db = 'hsnuwp'
charset = 'utf8'
protocol = 'tcp'

connection = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             password=passwd,
                             db=db,
                             # protocol=protocol,
                             charset=charset)

# create cursor
cursor = connection.cursor()


def get_posts(length):
     """This function send request to ACF REST API.

        Args:
            length (int): Number of post you want to get (-1 for all posts)

        Returns:

        """

    # SQL
    if length == -1:
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time ASC'
    else:
        sql = 'SELECT * FROM `wp_btaeon_msgs` ORDER BY msg_time DESC ' + 'LIMIT ' + length

    # 執行語法
    cursor.execute(sql)
    # all result
    data = cursor.fetchall()

    return_dict = [{}, {}, {}]
    return 0

# 關閉連線
connection.close()
