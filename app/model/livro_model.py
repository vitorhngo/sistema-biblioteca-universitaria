from dotenv import load_dotenv
import os

load_dotenv()  

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

import psycopg2

class LivroModel:
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
            self.cursor.execute("SELECT * FROM livro ORDER BY id;")
            return self.cursor.fetchall()
        
        except Exception as e:
            print(f"\nErro ao listar livros: {e}\n")
            return []
    
    def inserir(self, resposta: list):
        id_autor = resposta[0]
        titulo = resposta[1]
        data_publicacao = resposta[2]
        try:
            self.cursor.execute("INSERT INTO livro (id_autor, titulo, data_publicacao) VALUES (%s,%s,%s);", (id_autor, titulo, data_publicacao))
            self.conn.commit()
            return {'sucesso': True}
        
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : f"Falha na integridade nos dados. {e}"
                }
        
    def existe_id(self, id, entidade):
        try:
            self.cursor.execute(f"SELECT 1 FROM {entidade} WHERE id=%s;", (id,))
            resultado = self.cursor.fetchone()
            if resultado:
                return {'sucesso':True}
            else:
                return {'sucesso': False, 'erro': f"Nenhum {entidade} encontrado com esse ID."}

        except Exception as e:
            print(f"\nErro ao verificar a existência do {entidade}: {e}\n")
            return {'sucesso': False, 'erro': e}

    def existe_id_livro(self, id_livro):
        return self.existe_id(id_livro, 'livro')

    def existe_id_autor(self, id_autor):
        return self.existe_id(id_autor, 'autor')

    #FIX: O método exite_id retornava um valor inconsistente. O bug foi resolvido.
    def atualizar(self, resposta: list):
        id_livro = resposta[0]
        id_autor = resposta[1]
        titulo = resposta[2]
        data_publicacao = resposta[3]
        try:
            id_existe_livro = self.existe_id_livro(id_livro)
            if not id_existe_livro['sucesso']:
                return id_existe_livro

            id_existe_autor = self.existe_id_autor(id_autor)
            if not id_existe_autor['sucesso']:
                return id_existe_autor

            self.cursor.execute("UPDATE livro SET id_autor= %s, titulo= %s, data_publicacao= %s WHERE id= %s;", (id_autor, titulo, data_publicacao, id_livro))
            self.conn.commit()
            return {'sucesso': True}
        
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return {
                'sucesso': False, 
                'erro' : f"Falha na integridade nos dados. {e}"
                }
    
    def excluir(self, id_livro) -> dict:
        try:
            id_existe = self.existe_id_livro(id_livro)
            if not id_existe['sucesso']:
                return id_existe
            
            self.cursor.execute("DELETE FROM livro WHERE id= %s;", (id_livro,))
            self.conn.commit()
            return {'sucesso': True}
        
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
    
    