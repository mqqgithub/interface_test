'''
python操作oracle数据库需要使用到cx-oracle库。
主要如果按照的oracle客户端是32bit就会报错
安装：pip install cx-oracle
python连接oracle数据库分以下步骤：
1、与oracle建立连接；

2、获取游标；

3、执行sql语句；

4、fetch查询结果或commit修改结果；

5、关闭游标；

6、关闭oracle连接。
'''
import cx_Oracle as oracle

def readOracleData():
    # connect oracle database
    db = oracle.connect('qadev/ckjtpay12@T_KJTPAY')
    # create cursor
    cursor = db.cursor()
    # execute sql
    cursor.execute('select sysdate from dual')
    # fetch data
    data = cursor.fetchone()
    print('Database time:%s' % data)
    # close cursor and oracle
    cursor.close()
    db.close()

if __name__ == '__main__':
    #sql = """select t.*,rowid from ch_info_dictitem t where t.groupid=:1"""
    #params = ('WorkFlowCategory', )
    #print(execute_oracle_sql_query(sql=sql, params=params))
    readOracleData()




