from dotenv import load_dotenv
import os

load_dotenv()  

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

import psycopg2
from psycopg2 import errors

class AutorModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname=database,
                user=user,
                password=password,
                host=host,
                port=port
            )

            self.cursor = self.conn.cursor()
            
        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}\n")

    def listar(self):
        try:
            self.cursor.execute("SELECT * FROM autor ORDER BY id;")
            return self.cursor.fetchall()
        
        except Exception as e:
            print(f"\nErro ao listar autores: {e}\n")
            return []
    
    def inserir(self, resposta: list):
        nome = resposta[0]
        nacionalidade = resposta[1]
        try:
            self.cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s,%s);", (nome, nacionalidade))
            self.conn.commit()
            return {'sucesso': True}
        
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : f"Falha na integridade nos dados. {e}"
                }

    def existe_id(self, id_autor):
        try:
            self.cursor.execute("SELECT 1 FROM autor WHERE id=%s;", (id_autor,))
            resultado = self.cursor.fetchone()
            if resultado:
                return {'sucesso':True}
            else:
                return {'sucesso': False, 'erro': "Nenhum autor encontrado com esse ID."}

        except Exception as e:
            print(f"\nErro ao verificar a existência do autor: {e}\n")
            return {'sucesso': False, 'erro': e}
        
    def atualizar(self, resposta: list):
        id_autor = resposta[0]
        nome = resposta[1]
        nacionalidade = resposta[2]
        try:
            id_existe = self.existe_id(id_autor)
            if not id_existe['sucesso']:
                return id_existe

            self.cursor.execute("UPDATE autor SET nome= %s, nacionalidade= %s WHERE id= %s;", (nome, nacionalidade, id_autor))
            self.conn.commit()
            return {'sucesso': True}
        
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : f"Falha na integridade nos dados. {e}"
                }
    
    def excluir(self, id_autor) -> dict:
        try:
            id_existe = self.existe_id(id_autor)
            if not id_existe['sucesso']:
                return id_existe
        
            self.cursor.execute("DELETE FROM autor WHERE id= %s;", (id_autor,))
            self.conn.commit()
            return {'sucesso': True}
        
        except errors.ForeignKeyViolation:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : "Não é possível excluir este autor porque ele possui livros vinculados no sistema.\nDica: Remova ou altere os livros deste autor antes de excluí-lo."
                }
        
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : f"Falha na integridade nos dados. {e}"
                }
        
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()
    
    