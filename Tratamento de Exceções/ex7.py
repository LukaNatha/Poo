def verificar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError(f"Nota inválida: deve estar entre 0 e 10. (Recebido: {nota})")
    
    print(f"Nota {nota} validada com sucesso!")
    return nota

try:
    verificar_nota(8.5)
    verificar_nota(12)
except ValueError as e:
    print(f"Erro capturado: {e}")