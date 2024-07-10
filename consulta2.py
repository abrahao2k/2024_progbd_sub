import mariadb    #importar o driver
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="vendas")  #conectar ao db
cursor = conexao.cursor()  #criar cursor

nome = input("Digite o nome do cliente para pesquisar: ")

# executar uma consulta
cursor.execute(f"SELECT * FROM clientes WHERE nome LIKE '%{nome}%' ")

for linha in cursor:
    print(linha)    #mostra todos os dados de uma linha

cursor.close()  # finaliza a conexão
conexao.close() # finaliza a conexão
