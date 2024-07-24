import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="estoque")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")
for linha in cursor:
    print("Codigo: ", linha[0])
    print("Nome: ", linha[1])
    print("Preço: ", linha[2])
    print("Estoque: ", linha[3])
    print("------------------------------------")

cod = input("Digite o código do produto que deseja alterar: ")
cursor.execute("SELECT * FROM produtos WHERE codigo = " + cod)
if cursor.rowcount == 0 :
    print("CÓDIGO NÃO ENCONTRADO")
else:
    for linha in cursor:
        print("nome:", linha[1])
        print("preco:", linha[2])
        print("estoque:", linha[3])
    
    col = input("Qual coluna deseja alterar? ")
        
    if col in ('nome', 'preco', 'estoque'):
        nova = input("Digite a nova informação: ")
        cursor.execute(
            f"UPDATE produtos SET {col} = '{nova}' WHERE codigo = {cod}")
        conexao.commit()
        print("Informação atualizada com sucesso!")
    else:
        print("Coluna inválida.")

cursor.close()
conexao.close()