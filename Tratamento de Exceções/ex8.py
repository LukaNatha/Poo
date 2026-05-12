def simular_arquivo():
    print("Abrindo arquivo...")
    try:
        print("Processando dados...")
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro detectado: Não é possível dividir por zero!")
    finally:
        print("Fechando arquivo...")

simular_arquivo()