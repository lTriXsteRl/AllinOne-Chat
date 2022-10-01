#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import sqlite3
from time import time
import json

db = sqlite3.connect("python-back/Ain1chat.sqlite3")



def registration(mail, login, password):
    global db
    cursor = db.cursor()
    #check mail exist
    res = cursor.execute("""select * from users where mail='%s'"""%(mail)).fetchall()
    if len(res)!=0:
        print(r'{"return":1, "text":"Error! Mail already used!"}')
    #check user exist
    res = cursor.execute("""select * from users where login='%s'"""%(login)).fetchall()
    if len(res)!=0:
        print(r'{"return":2, "text":"Error! User is exist!"}')
    #user not exist
    else:
        #register
        res = cursor.execute("""insert into users(login,password,mail) values('%s', '%s','%s') returning id"""\
            %(login,password,mail)).fetchall()
        #check existing new user
        if len(res)>0:
            print(r'{"return":0, "text":"User register successfully", "id":%d}'%(res[0][0]))
            db.commit()
        else:
            print(r'{"return":3, "text":"Error! Register failed!"}')
    cursor.close()
    
#функция логина пока чисто символическая, возвращаю id из бд
def auth(login, password):
    global db
    cursor = db.cursor()
    #check user exist
    res = cursor.execute("""select id,password,name,img from users where login='%s'"""%(login)).fetchall()
    #user not exist
    if len(res)==0:
        print(r'{"return":1, "text":"Error! User is not exist!"}')
    #user exist, but incorrect password
    elif password != res[0][1]:
        print(r'{"return":2, "text":"Error! Incorrect password!"}')
    #user exist, password is correct. login successfull
    else:
        #handle no img and no nickname
        res = list(res[0])
        if res[2]==None: res[2]=login
        if res[3]==None: res[3]=''

        print(r'{"return":0, "text":"Login successfull.", "id":%d, "nickname":"%s", "img":"%s"}'%(res[0],res[2],res[3]))
    cursor.close()



def listChats(idUser):
    global db
    cursor = db.cursor()
    #check user exist
    res = cursor.execute("""select id_chat from contacts where id_user='%d'"""%(idUser)).fetchall()
    for x in range(len(res)):
        res[x] = res[x][0]
    
    print(r'{"return":0, "text":"Return list chats id", "id chats":%s}'%(str(res)))

    cursor.close()


#добавить проверку что юзеры существуют
def createChat(listIdUsers, name, img=''):
    global db
    cursor = db.cursor()
    #create chat
    res = cursor.execute("""insert into chats(name,img) values('%s', '%s') returning id"""%(name,img)).fetchall()
    #failed create chat
    if len(res)==0:
        print(r'{"return":1, "text":"Error! Failed create chat!"}')
    #successfull create chat
    else:
        id = res[-1][0]
        #add users in chat
        cntr=0
        for idUser in listIdUsers:
            res = cursor.execute("""insert into contacts(id_user,id_chat) values(%d, %d) returning id"""%(idUser,id)).fetchall()
            #check correcting add users
            if len(res)!=0: cntr+=1
        #add users successfull
        if cntr==len(listIdUsers):
            print(r'{"return":0, "text":"Successfull create chat.", "id chat":%d, "id users":%s}'%(id,str(listIdUsers)))
            db.commit()
        #failed add users
        else:
            print(r'{"return":2, "text":"Error! Failed add users to chat"}')
    cursor.close()

#attachment files must be list of strings. 
#text and attachment are optional, but one of this is requirement
def createMessage(idUser,idChat,text='',attachment=[]):
    if type(text)!=str or type(attachment)!=list:
        print(r'{"return":1, "text":"Error! Incorrect type data"}')
    if len(text)==0 and len(attachment)==0:
        print(r'{"return":2, "text":"Error! Empty message"}')
    else:
        global db
        cursor = db.cursor()
       
        msgJson = {
            'type'          :'msg',     
            'attachment'    :attachment,
            'text'          :text
        }
        # msgJson = {
        #     'type'          :'reference',
        #     'id'            :id
        # }

        res = cursor.execute("""insert into messages(sender,chat,timestamp,json) values(%d,%d,%d,'%s') returning id"""\
            %(idUser,idChat,time(),json.dumps(msgJson))).fetchall()
        #failed create msg
        if len(res)==0:
            print(r'{"return":3, "text":"Error! Failed create message"}')
        else:
            print(r'{"return":0, "text":"Successfull create message", "id":%d}'%(res[0][0]))
        db.commit()
        cursor.close()


# registration('user3@allinone.com','user3','user3')
# auth('user3', 'user3')
# createChat([1,2], "chatik2", img='')
# listChats(1)
createMessage(6,1,'hello world')
createMessage(6,1,attachment=["qweqweq"])


db.close()
