# importar o driver
import mariadb

# estabelecer a conexao com o bd
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="contatos")

# criar um cursor (objeto que executa comandos SQL)
cursor = conexao.cursor()

# digitar os dados a serem gravados no BD
nome = input("Digite o nome: ")
fone = input("Digite o telefone: ")

# executar um comando SQL com as variáveis digitadas
cursor.execute(f"INSERT INTO pessoas VALUES(null, '{nome}', '{fone}')")

#confirmar a gravação no bd
conexao.commit()
print("Gravado com sucesso.")

# Encerrar a conexao
cursor.close()
conexao.close()
print("Conexão finalizada.")