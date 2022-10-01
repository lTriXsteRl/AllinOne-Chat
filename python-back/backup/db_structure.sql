--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.2 в сб окт. 1 19:29:29 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: chats
CREATE TABLE chats (id INT (32) PRIMARY KEY, name STRING (50), img STRING (50));

-- Таблица: contacts
CREATE TABLE contacts (id INT (32) PRIMARY KEY, id_user INT (4) REFERENCES users (id), id_chat INT (4) REFERENCES chats (id));

-- Таблица: messages
CREATE TABLE messages (id INT (32) PRIMARY KEY, sender INT (4) REFERENCES users (id) NOT NULL, chat INTEGER (4) REFERENCES chats (id) NOT NULL, timestamp INT (4) NOT NULL, json STRING NOT NULL);

-- Таблица: users
CREATE TABLE users (
    id       INTEGER     PRIMARY KEY AUTOINCREMENT,
    login    STRING (50) UNIQUE
                         NOT NULL,
    password STRING (50) NOT NULL,
    mail     STRING (50),
    name     STRING (50),
    img      STRING (50) 
);

-- Индекс: msg_chat
CREATE INDEX msg_chat ON messages (chat);

-- Индекс: msg_sender
CREATE INDEX msg_sender ON messages (sender);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
