import sqlite3
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

from config import DB_PATH

def connect_db():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_usuario(nome, senha):
    """Adiciona um usuário ao banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, senha) 
        VALUES (?, ?)
    ''', (nome, senha))  # Usando parâmetro para evitar SQL Injection
    conn.commit()
    conn.close()

def get_usuarios():
    """Retorna todos os usuários do banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, senha FROM usuarios')
    usuarios = cursor.fetchall()  # Retorna todos os registros
    conn.close()
    return usuarios

usuarios = get_usuarios()
id, name, password = usuarios[0]