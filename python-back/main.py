#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect("python-back/Ain1chat.sqlite3")



def registration(mail, login, password):
    global db
    cursor = db.cursor()
    #check mail exist
    res = cursor.execute("""select * from users where mail='%s'"""%(mail))
    if len(res.fetchall())!=0:
        print(r'{"return":1, "text":"Error! Mail already used!"}')
    #check user exist
    res = cursor.execute("""select * from users where login='%s'"""%(login))
    if len(res.fetchall())!=0:
        print(r'{"return":2, "text":"Error! User is exist!"}')
    #user not exist
    else:
        #register
        res = cursor.execute("""insert into users(login,password,mail) values('%s', '%s','%s')"""%(login,password,mail))
        db.commit()
        #check existing new user
        res = cursor.execute("""select id from users where login='%s'"""%(login))
        res = res.fetchall()
        if len(res)>0:
            print(r'{"return":0, "text":"User register successfully", "id":%d}'%(res[0][0]))
        else:
            print(r'{"return":3, "text":"Error! Register failed!"}')
    cursor.close()
    
#функция логина пока чисто символическая, возвращаю id из бд
def auth(login, password):
    global db
    cursor = db.cursor()
    #check user exist
    res = cursor.execute("""select id,password,name,img from users where login='%s'"""%(login))
    res = res.fetchall()[0]
    #user not exist
    if len(res)==0:
        print(r'{"return":1, "text":"Error! User is not exist!"}')
    #user exist, but incorrect password
    elif password != res[1]:
        print(r'{"return":2, "text":"Error! Incorrect password!"}')
    #user exist, password is correct. login successfull
    else:
        #handle no img and no nickname
        res = list(res)
        if res[2]==None: res[2]=login
        if res[3]==None: res[3]=''
        
        print(r'{"return":0, "text":"Login successfull.", "id":%d, "nickname":"%s", "img":"%s"}'%(res[0],res[2],res[3]))

# registration('admin@admin.com','admin','admin')
auth('admin', 'admin')

db.close()