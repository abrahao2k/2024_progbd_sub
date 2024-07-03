# importar o driver
import mariadb

# estabelecer a conexao com o bd
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="contatos")

# criar um cursor (objeto que executa comandos SQL)
cursor = conexao.cursor()

# executar um comando SQL
cursor.execute("INSERT INTO pessoas VALUES(2, 'Beto', '3321-4577')")

#confirmar a gravação no bd
conexao.commit()
print("Gravado com sucesso.")

# Encerrar a conexao
cursor.close()
conexao.close()
print("Conexão finalizada.")