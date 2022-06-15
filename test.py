# 用pymysql连接尝试
import pymysql 
# 连接数据库
# "mysql://tess@139.196.51.214:3366/tess?charset=utf8"
conn = pymysql.connect(
	host = '139.196.51.214',
	port = 3366,
	user = 'root',
	password = '123456',
	db = 'tess',
	charset='utf8'
	)
cur = conn.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchall()

print(data)

# 关闭数据库连接
conn.close()
