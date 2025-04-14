import mysql.connector


def cria_branco(nome):

    conn= mysql.connector.connect(
        host="",
        user="admin",
        password=""
    )

    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {nome}")



def connection_db():
    try:
        conn = mysql.connector.connect(
            database="mercado",
            user="admin",
            password="",
            host="",  
            port=3306
        )
        cur = conn.cursor()
        return conn,cur
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return None, None

def create_table():
    conn,cur = connection_db()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ITENS (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NOME VARCHAR(50),
                VALOR FLOAT
            );
        """)
    except mysql.connector.Error as err:
        print("Erro ao criar a tabela:", err)
   
def InsereDados(nome, valor):
    conn,cur = connection_db()
   
    try:
        create_table()
        cur.execute("INSERT INTO ITENS (NOME, VALOR) VALUES (%s, %s)", (nome, valor))
        conn.commit()
        
    except mysql.connector.Error as err:
        print("Erro ao inserir dados:", err)

def ObtemDados():
    conn,cur = connection_db()
    try:
        cur.execute("SELECT * FROM ITENS;")
        resultados = cur.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print("Erro ao obter dados:", err)
        return []
