import pymysql

host = 'shen.bike'
port = 3307
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


# 建立操作游標
cursor = connection.cursor()
# SQL語法（查詢資料庫版本）
sql = 'SELECT VERSION()'
# 執行語法
cursor.execute(sql)
# 選取第一筆結果
data = cursor.fetchone()

print("Database version : %s " % data)
# 關閉連線
connection.close()
