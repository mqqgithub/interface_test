import pymysql

# 打开数据库连接
#db = pymysql.connect("10.251.7.217:3306", "reconcileuser", "Kjt8(Sinver9)Haier7*", "c1reconciledb.kjtpay.c1prod")
def get_mysql_data():
    config = {
        'host': '10.251.7.217',
        'port': 3306,
        'user': 'reconcileuser',
        'passwd': 'Kjt8(Sinver9)Haier7*',
        'charset':'utf8mb4',
        #'db':'c1reconciledb.kjtpay.c1prod', 此处不需要，不然那会报错
        'cursorclass': pymysql.cursors.DictCursor,   #返回字典类型
        'connect_timeout': 10  #超时时间是10
        }
    conn = pymysql.connect(**config)
    conn.autocommit(1)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cur.execute("SELECT * FROM reconcilecore.pboc_reconcile_detail")
    return cur.fetchall()
    # 使用 fetchone() 方法获取单条数据.
    # 使用 fetchall() 获取多条数据

    # 关闭数据库连接
    cur.close()
    conn.close()


if __name__ == "__main__":
   data=get_mysql_data()
   for r in data:
       print(r)
