import mariadb    #importar o driver
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="vendas")  #conectar ao db
cursor = conexao.cursor()  #criar cursor
#######################################################################
print("MENU\n 1-Listar clientes \n 2-Listar saldos")
opcao = int(input("Opção? "))

if opcao == 1 :
    cursor.execute("SELECT nome FROM clientes ORDER BY nome")
    for linha in cursor:
        print(linha[0])
    
elif opcao == 2:
    cursor.execute(
        "SELECT saldo, nome from clientes WHERE saldo > 0 ORDER BY saldo DESC")
    for linha in cursor:
        print(f"R$ {linha[0]} - {linha[1]}")

######################################################################
cursor.close()  # finaliza a conexão
conexao.close() # finaliza a conexão
