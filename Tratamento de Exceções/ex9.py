class SenhaCurtaError(Exception):
    pass

def cadastrar_senha(senha):
    if len(senha) < 8:
        raise SenhaCurtaError(f"A senha fornecida tem apenas {len(senha)} caracteres. O mínimo é 8.")
    
    print("Senha cadastrada com sucesso!")


try:
    minha_senha = input("Digite uma nova senha: ")
    cadastrar_senha(minha_senha)
except SenhaCurtaError as erro:
    print(f"Falha no cadastro: {erro}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")