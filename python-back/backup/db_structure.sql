--
-- ���� ������������ � ������� SQLiteStudio v3.3.2 � �� ���. 1 20:38:31 2022
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: chats
CREATE TABLE chats (
    id   INTEGER     PRIMARY KEY AUTOINCREMENT,
    name STRING (50),
    img  STRING (50) 
);

-- �������: contacts
CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, id_user INTEGER REFERENCES users (id), id_chat INTEGER REFERENCES chats (id));

-- �������: messages
CREATE TABLE messages (id INTEGER PRIMARY KEY AUTOINCREMENT, sender INTEGER REFERENCES users (id) NOT NULL, chat INTEGER REFERENCES chats (id) NOT NULL, timestamp INT (4) NOT NULL, json STRING NOT NULL);

-- �������: users
CREATE TABLE users (
    id       INTEGER     PRIMARY KEY AUTOINCREMENT,
    login    STRING (50) UNIQUE
                         NOT NULL,
    password STRING (50) NOT NULL,
    mail     STRING (50),
    name     STRING (50),
    img      STRING (50) 
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
