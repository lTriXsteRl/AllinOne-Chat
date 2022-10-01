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
    cursor.close()



def listChats(idUser):
    global db
    cursor = db.cursor()
    #check user exist
    res = cursor.execute("""select id_chat from contacts where id_user='%d'"""%(idUser))
    res = res.fetchall()
    for x in range(len(res)):
        res[x] = res[x][0]
    
    print(r'{"return":0, "text":"Return list chats id", "id chats":%s}'%(str(res)))

    cursor.close()


#добавить проверку что юзеры существуют
def createChat(listIdUsers, name, img=''):
    global db
    cursor = db.cursor()
    #create chat
    res = cursor.execute("""insert into chats(name,img) values('%s', '%s')"""%(name,img))
    db.commit()
    res = cursor.execute("""select id from chats where name='%s'"""%(name))
    res = res.fetchall()
    #failed create chat
    if len(res)==0:
        print(r'{"return":1, "text":"Error! Failed create chat!"}')
    #successfull create chat
    else:
        id = res[-1][0]
        #add users in chat
        for userId in listIdUsers:
            res = cursor.execute("""insert into contacts(id_user,id_chat) values(%d, %d)"""%(userId,id))
        db.commit()
        #check correcting add users
        res = cursor.execute("""select id_user from contacts where id_chat=%d"""%(id))
        res = res.fetchall()
        #add users successfull
        if len(res)==len(listIdUsers):
            print(r'{"return":0, "text":"Successfull create chat.", "id chat":%d, "id users":%s}'%(id,str(listIdUsers)))
        #failed add users
        else:
            print(r'{"return":2, "text":"Error! Failed add users to chat"}')
    cursor.close()

# registration('admin@admin.com','admin','admin')
# auth('admin', 'admin')
# createChat([1,6], "chatik", img='')
listChats(6)


db.close()