import sqlite3

class db:
    cursor:''   # 游标
    conn:''     # 数据库连接

    def __init__(self):
        self.conn = sqlite3.connect("chat.db",check_same_thread = False)
        self.cursor = self.conn.cursor()
        # 如果不存在用户表则创建用户表
        sql = "create table if not exists scores (id integer primary key autoincrement,stu VARCHAR(20),course VARCHAR(20),score DOUBLE)"
        self.cursor.execute(sql)        # 执行sql语句

