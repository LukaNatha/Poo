def registrar_log(mensagem):
    arquivo = open("sistema.log", "a")
    arquivo.write(mensagem + "\n")
    arquivo.close()

registrar_log("Sistema iniciado com sucesso.")
registrar_log("Usuário 'admin' realizou login.")
registrar_log("Erro de conexão com o banco de dados.")

print("Mensagens de log registradas com sucesso no arquivo sistema.log!")
