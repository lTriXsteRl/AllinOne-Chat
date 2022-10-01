--
-- ���� ������������ � ������� SQLiteStudio v3.3.2 � �� ���. 1 19:29:29 2022
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: chats
CREATE TABLE chats (id INT (32) PRIMARY KEY, name STRING (50), img STRING (50));

-- �������: contacts
CREATE TABLE contacts (id INT (32) PRIMARY KEY, id_user INT (4) REFERENCES users (id), id_chat INT (4) REFERENCES chats (id));

-- �������: messages
CREATE TABLE messages (id INT (32) PRIMARY KEY, sender INT (4) REFERENCES users (id) NOT NULL, chat INTEGER (4) REFERENCES chats (id) NOT NULL, timestamp INT (4) NOT NULL, json STRING NOT NULL);

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

-- ������: msg_chat
CREATE INDEX msg_chat ON messages (chat);

-- ������: msg_sender
CREATE INDEX msg_sender ON messages (sender);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
