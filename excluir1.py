import mariadb
conexao = mariadb.connect(host="localhost", user="root", password="", database="estoque")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")
for linha in cursor:
    print("Codigo: ", linha[0])
    print("Nome: ", linha[1])
    print("Preço: ", linha[2])
    print("Estoque: ", linha[3])
    print("------------------------------------")

cod = input("Digite o código do produto que deseja excluir: ")
cursor.execute("SELECT * FROM produtos WHERE codigo = " + cod)
if cursor.rowcount == 0 :
    print("CÓDIGO NÃO ENCONTRADO")
else:
    for linha in cursor: print(linha)
    
    resp = input("Deseja realmente excluir? (s/n) ")
    if resp == "s" :
        cursor.execute("DELETE FROM produtos WHERE codigo = " + cod)
        conexao.commit()
        print("PRODUTO EXCLUÍDO COM SUCESSO!")
    else:
        print("NENHUM PRODUTO FOI EXCLUIDO.")
