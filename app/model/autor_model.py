from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

import psycopg2

class AutorModel:

    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="biblioteca_universitaria",
                user="postgres",
                password="  "
            )
        except Exception as e:
            print("Erro ao conectar ao banco:", e)

    def inserir_autor(self, nome, nacionalidade):
            try:
                cursor = self.conexao.cursor()
                cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s);", (nome, nacionalidade))
                self.conexao.commit()
                cursor.close()
            except Exception as e:
                print("Erro ao inserir autor:", e)
                self.conexao.rollback()

    def listar_autores(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, nacionalidade FROM autor ORDER BY id;")
            autor = cursor.fetchall()
            cursor.close()
            return autor
        except Exception as e:
            print("Erro ao listar autores:", e)
            return []

    def atualizar_autor(self, id_autor, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s;", (nome, nacionalidade, id_autor))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao atualizar autor:", e)
            self.conexao.rollback()

    def excluir_autor(self, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id = %s;", (id_autor,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao excluir autor:", e)
            self.conexao.rollback()

    # Após a função excluir_autor, 
    # inserir uma função para voltar ao menu principal