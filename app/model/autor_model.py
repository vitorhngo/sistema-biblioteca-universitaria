# from dotenv import load_dotenv
# import os

# load_dotenv()  

# host = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")
# database = os.getenv("DB_NAME")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")

import psycopg2

class AutorModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="biblioteca_universitaria",
                user="postgres",
                password="65266256",
                host="localhost",
                port="5432"
            )

            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}\n")

    def listar(self):
        try:
            self.cursor.execute("select * from autor order by id;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar autores: {e}\n")
            return []
    
    def inserir(self, resposta: list):
        try:
            self.cursor.execute("insert into autor (nome, nacionalidade) values (%s,%s);", (resposta[0], resposta[1]))
            self.conn.commit()
        except Exception as e:
            print(f"\nErro ao inserir autor: {e}\n")
            self.conn.rollback()

    def existe_id(self, id_autor): #  Pode ser que aqui ao invés de 'id_autor', seja somente 'id'
        try:
            self.cursor.execute("select 1 from autor where id=%s;", (id_autor,))
            return self.cursor.fetchone is not None
        except Exception as e:
            print(f"\nErro ao verificar a existência do autor: {e}\n")
            return False
        
    def atualizar(self, resposta: list): # Mesma lógica acima, aqui pode ser que 'id_autor' dê errado
        id_autor = resposta[0]
        nome = resposta[1]
        nacionalidade = resposta[2]
        try:
            if not self.existe_id(resposta[0]):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False
        
            self.cursor.execute("update autor set nome= %s, nacionalidade= %s where id= %s;", (nome, nacionalidade, id_autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao atualizar autor: {e}\n")
            self.conn.rollback()
            return False
    
    def excluir(self, id_autor):
        try:
            if not self.existe_id(id_autor):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False
        
            self.cursor.execute("delete from autor where id= %s;", (id_autor,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao excluir autor: {e}\n")
            self.conn.rollback()
            return False
        
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()
    
    