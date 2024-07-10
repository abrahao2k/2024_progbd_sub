import mariadb    #importar o driver
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="vendas")  #conectar ao db
cursor = conexao.cursor()  #criar cursor

cidade = input("Digite a cidade: ")

# executar uma consulta
cursor.execute(f"SELECT * FROM clientes WHERE cidade = '{cidade}' ")

for linha in cursor:
    print(f"{linha[2]} - {linha[1]}")

print(f"{cursor.rowcount} resultados encontrados.")

cursor.close()  # finaliza a conexão
conexao.close() # finaliza a conexão
