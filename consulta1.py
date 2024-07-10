import mariadb    #importar o driver
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="vendas")  #conectar ao db
cursor = conexao.cursor()  #criar cursor

# executar uma consulta
cursor.execute("SELECT * FROM clientes")

for linha in cursor:
    #print(linha)    #mostra todos os dados de uma linha
    #print(linha[1])  #mostra só o nome do cliente (posição 1 da tupla)
    print(f"{linha[1]} - {linha[2]}")  #mostra o nome e a cidade

