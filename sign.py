import sqlite3, getpass


# 用户登录
def showdate(username):
    sql = sqlite3.connect('user.db')
    data = sql.execute("select * from user where username='%s'" % username).fetchone()
    sql.close()
    return data


def val():
    while 1:
        name = input("用户名:")  # 输入用户名
        data = showdate(name)  # 获取用户名对应的数据库资料
        if data:
            passworld = input('密码:')
            if data[2] == passworld:

                print("登录成功")
                break
            else:
                print("密码错误")
        else:
            print("用户名不存在")