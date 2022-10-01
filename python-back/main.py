#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect("python-back/Ain1chat.sqlite3")



def registration(mail, login, password):
    global db
    cursor = db.cursor()
    res = cursor.execute("""select * from users where mail='%s'"""%(mail))
    if len(res.fetchall())!=0:
        print(r'{"return":1, "text":"Error! Mail already used!"}')
    res = cursor.execute("""select * from users where login='%s'"""%(login))
    #user exist
    if len(res.fetchall())!=0:
        print(r'{"return":2, "text":"Error! User is exist!"}')
        pass
    #user not exist
    else:
        res = cursor.execute("""insert into users(login,password,mail) values('%s', '%s','%s')"""%(login,password,mail))
        db.commit()
        res = cursor.execute("""select id from users where login='%s'"""%(login))
        res = res.fetchall()
        if len(res)>0:
            print(r'{"return":0, "text":"User register successfully", "id":%d}'%(res[0][0]))
        else:
            print(r'{"return":3, "text":"Error! Register failed!"}')

        
    cursor.close()
    
    

registration('admin@admin.com','admin','admin')


db.close()